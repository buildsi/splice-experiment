#!/usr/bin/env python3

import argparse
import os
import random
import re
import json
import sys
import tempfile

import yaml

here = os.path.dirname(os.path.abspath(__file__))

# This is intended to run in the container
template = """#!/bin/bash 

. /spack/share/spack/setup-env.sh 

# always build with debug
export SPACK_ADD_DEBUG_FLAGS=true

"""

# This is to submit the job
submit_template = """#!/bin/bash 

%s
"""

docker_template = "%s run -v %s:/cache -v %s:/spack/opt -v %s:/results -it %s %s"
singularity_template = "singularity exec --containall --home $PWD --bind %s:/cache --bind %s:/spack/opt %s %s"


def get_parser():
    parser = argparse.ArgumentParser(
        description="Spliced Experiment Submitter",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "experiment_dir", help="directory with experiments.yaml to discover"
    )
    parser.add_argument(
        "sif",
        help="Full path to submit container.",
        default="spliced-experiment_latest.sif",
        nargs="?",
    )
    parser.add_argument(
        "--outdir", help="Output directory for results", default="results"
    )
    parser.add_argument(
        "--spack-opt",
        dest="spack_opt",
        help="Full path to spack opt (empty to start) to bind.",
        default="spack-opt",
    )
    parser.add_argument(
        "--dry-run",
        help="Show container run commands only",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--skip-smeagle",
        help="Skip running smeagle",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--single",
        help="Show a single command for each",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--json",
        help="Dump commands as json instead (also writes to GitHub output)",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--docker",
        help="Show docker command instead",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--podman",
        help="Use podman instead",
        default=False,
        action="store_true",
    )
    parser.add_argument("-N", help="number of commands to run or generate")
    parser.add_argument(
        "--pattern", help="match this pattern to discover an experiment."
    )

    parser.add_argument(
        "--cache",
        help="Full path to predictor cache (empty to start) to bind.",
        default="cache",
    )
    return parser


class ExperimentJobsGenerator:
    """
    Generate a matrix of jobs for an experiment.
    """

    def __init__(self, experiment_yaml, outdir, skip_smeagle=False):
        self.experiment = read_yaml(experiment_yaml)
        self.outdir = outdir
        self.experiment_name = os.path.basename(experiment_yaml).split(".")[0]
        self.skip_smeagle = skip_smeagle

    def generate_jobs(self):
        """
        Main entrypoint to generate jobs.
        """
        matrix = []

        # Versions across top level package
        if "versions" not in self.experiment["package"]:

            # One version (the dep name, versions extracted in job run)
            if "splice_versions" in self.experiment:
                for splice_version in self.experiment["splice_versions"]:
                    splice_version = "%s@%s" % (
                        self.experiment["splice"],
                        splice_version,
                    )
                    matrix.append(
                        self.generate_spliced_command(None, splice_version["name"])
                    )
            else:
                for splice_version in [self.experiment["splice"]]:
                    matrix.append(
                        self.generate_spliced_command(None, splice_version["name"])
                    )

        else:
            for version in self.experiment["package"]["versions"]:

                # One version (the dep name, versions extracted in job run)
                if "splice_versions" in self.experiment:
                    for splice_version in self.experiment["splice_versions"]:
                        splice_version = "%s@%s" % (
                            self.experiment["splice"],
                            splice_version["name"],
                        )
                        matrix.append(
                            self.generate_spliced_command(
                                version, splice_version["name"]
                            )
                        )
                else:
                    raise NotImplementedError
        return matrix

    def generate_spliced_command(self, version, splice_version):
        """
        Generate a command for a single experiment
        """
        # versioned package
        package = self.experiment["package"]["name"]
        outfile = os.path.join(
            "/results",
            self.experiment["package"]["name"],
            splice_version,
            "%s.json" % self.experiment_name,
        )

        if version:
            package = "%s@%s" % (self.experiment["package"]["name"], version)
            outfile = os.path.join(
                "/results",
                self.experiment["package"]["name"],
                version,
                splice_version,
                "%s.json" % self.experiment_name,
            )
        slug = "%s-%s-%s-%s" % (
            self.experiment["package"]["name"],
            version,
            splice_version,
            self.experiment_name,
        )
        # The command requires spack python from the getgo to get exactly what spack is settingup
        if "replace" in self.experiment:
            cmd = (
                "spack python /code/scripts/run_spliced.py diff --package %s --splice %s --runner spack --replace %s --experiment %s --outfile %s %s"
                % (
                    package,
                    splice_version,
                    self.experiment["replace"],
                    self.experiment["package"]["name"],
                    outfile,
                    "--skip" if self.skip_smeagle else "",
                )
            )
        else:
            cmd = (
                "spack python /code/scripts/run_spliced.py diff --package %s --splice %s --runner spack --experiment %s --outfile %s %s"
                % (
                    package,
                    splice_version,
                    self.experiment["package"]["name"],
                    outfile,
                    "--skip" if self.skip_smeagle else "",
                )
            )

        return {
            "command": cmd,
            "package": package,
            "runner": "spack",
            "splice": self.experiment["splice"],
            "replace": self.experiment.get("replace"),
            "experiment": self.experiment_name,
            "outfile": outfile,
            "outdir": os.path.dirname(outfile),
            "slug": slug,
        }


def recursive_find(base, pattern=None):
    """
    Find filenames that match a particular pattern, and yield them.
    """
    # We can identify modules by finding module.lua
    for root, folders, files in os.walk(base):
        for file in files:
            fullpath = os.path.abspath(os.path.join(root, file))

            if pattern and not re.search(pattern, fullpath):
                continue

            yield fullpath


def read_yaml(filename):
    with open(filename, "r") as fd:
        content = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return content


def main():

    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    if args.docker and args.podman:
        sys.exit("You can only choose one of --docker or --podman")

    experiment_dir = os.path.abspath(args.experiment_dir)
    container = os.path.abspath(args.sif)

    if not args.spack_opt or not args.cache:
        sys.exit("Both --spack-opt and --cache are required.")
    spack_opt = os.path.abspath(args.spack_opt)
    cache = os.path.abspath(args.cache)
    outdir = os.path.abspath(args.outdir)

    for path in experiment_dir, outdir:
        if not os.path.exists(path) and not args.dry_run and not args.json:
            sys.exit(f"{path} does not exist.")

    if args.docker or args.podman:
        container = "ghcr.io/buildsi/spliced-experiment:latest"
    elif args.sif:
        container = os.path.abspath(args.sif)
        if not args.dry_run and not args.json:
            assert os.path.exists(container)
    else:
        sys.exit(
            "A container is required for the third argument to run with Singularity."
        )

    # Make an output logs directory
    logs_dir = os.path.join(here, "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # create scripts submission directory
    scripts = os.path.abspath(os.path.join(here, "submit"))
    if not os.path.exists(scripts):
        os.makedirs(scripts)

    # We will build up a matrix of experiments
    # We will want to shuffle to not do the same builds at once
    matrix = []

    seen = set()

    # Recursively find experiments
    for experiment_yaml in recursive_find(experiment_dir, "experiment.yaml"):
        if args.pattern and not re.search(args.pattern, experiment_yaml):
            continue

        # The generator will derive versions, etc. and a matrix of jobs
        gen = ExperimentJobsGenerator(experiment_yaml, outdir, args.skip_smeagle)

        if args.single and gen.experiment["package"]["name"] in seen:
            continue
        seen.add(gen.experiment["package"]["name"])

        if args.single:
            matrix.append(gen.generate_jobs()[0])
        else:
            matrix += gen.generate_jobs()

    print("Generated %s jobs" % len(matrix))
    print("Shuffling...")
    random.shuffle(matrix)

    # Only print matrix to output (and GitHub actions output)
    if args.json:
        print(matrix)
        print("::set-output name=commands::%s\n" % json.dumps(matrix))
        return

    for i, entry in enumerate(matrix):

        if args.N and i == args.N:
            break

        tmpfile = os.path.join(scripts, "%s.sh" % entry["slug"])
        submitfile = os.path.join(scripts, "%s-submit.sh" % entry["slug"])
        outfile = os.path.join(logs_dir, "%s.out" % entry["slug"])

        # Dry run shows the testing command
        if args.dry_run:
            entrypoint = entry["command"]
        else:
            entrypoint = "/bin/bash " + tmpfile

        if args.docker or args.podman:
            container_templated = docker_template % (
                "docker" if args.docker else "podman",
                cache,
                spack_opt,
                outdir,
                container,
                entrypoint,
            )
        else:
            container_templated = singularity_template % (
                cache,
                spack_opt,
                container,
                entrypoint,
            )

        if args.dry_run:
            print(container_templated)
            continue

        if not os.path.exists(entry["outdir"]):
            os.makedirs(entry["outdir"])

        # Template to run (give to container as entrypoint) vs. submit script to run container
        templated = template + "\n" + entry["command"]
        submit_templated = submit_template % container_templated

        with open(tmpfile, "w") as fd:
            fd.writelines(templated)
        with open(submitfile, "w") as fd:
            fd.writelines(submit_templated)
        os.system(
            "sbatch --time 360 -A asi --out=%s -N 1 -n 1 --cpus-per-task=4 --err %s %s"
            % (outfile, outfile, submitfile)
        )


if __name__ == "__main__":
    main()
