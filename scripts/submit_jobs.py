#!/usr/bin/env python3

from spliced.client.command import get_package_versions, get_splice_versions
import spliced.experiment
import spliced.utils as utils
import argparse
import os
import random
import sys
import tempfile

here = os.path.dirname(os.path.abspath(__file__))

# This is intended to run in the container
template = """#!/bin/bash 

. /spack/share/spack/setup-env.sh 

# always build with debug
export SPACK_ADD_DEBUG_FLAGS=true

"""

# This is to submit the job
submit_template = """#!/bin/bash 

singularity exec -b %s:/cache -b %s:/spack/opt %s /bin/bash %s

"""


def get_parser():
    parser = argparse.ArgumentParser(
        description="Spliced Experiment Submitter",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "experiment_dir", help="directory with experiments.yaml to discover"
    )
    parser.add_argument("outdir", help="Output directory for results")
    parser.add_argument("sif", help="Full path to submit container.")
    parser.add_argument(
        "--spack-opt",
        dest="spack_opt",
        help="Full path to spack opt (empty to start) to bind.",
    )
    parser.add_argument(
        "--cache",
        help="Full path to predictor cache (empty to start) to bind.",
    )
    return parser


class ExperimentJobsGenerator:
    """
    Generate a matrix of jobs for an experiment.
    """

    def __init__(self, experiment_yaml, outdir):
        self.experiment_yaml = experiment_yaml
        self.experiment = spliced.experiment.Experiment()
        self.experiment.load(experiment_yaml)
        self.outdir = outdir

    def generate_jobs(self):
        """
        Main entrypoint to generate jobs.
        """
        versions = get_package_versions(self.experiment.package)
        splice_versions = get_splice_versions(self.experiment)

        matrix = []
        for version in versions:
            for splice_version in splice_versions:
                matrix.append(self.generate_spliced_command(version, splice_version))
        return matrix

    def generate_spliced_command(self, version, splice_version):
        """
        Generate a command fora single experiment
        """
        # versioned package
        package = "%s@%s" % (self.experiment.package, version)
        outfile = os.path.join(
            self.outdir,
            self.experiment.package,
            version,
            splice_version,
            "%s.json" % self.experiment.name,
        )
        slug = "%s-%s-%s-%s" % (
            self.experiment.package,
            version,
            splice_version,
            self.experiment.name,
        )
        cmd = (
            "spliced splice --package %s --splice %s --runner spack --replace %s --experiment %s --outfile %s"
            % (
                package,
                splice_version,
                self.experiment.replace,
                self.experiment.name,
                outfile,
            )
        )

        return {
            "command": cmd,
            "package": package,
            "runner": "spack",
            "splice": self.experiment.splice,
            "replace": self.experiment.replace,
            "experiment": self.experiment.name,
            "outfile": outfile,
            "outdir": os.path.dirname(outfile),
            "slug": slug,
        }


def main():

    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    experiment_dir = os.path.abspath(args.experiment_dir)
    outdir = os.path.abspath(args.outdir)
    container = os.path.abspath(args.sif)

    if not args.spack_opt or not args.cache:
        sys.exit("Both --spack-opt and --cache are required.")
    spack_opt = os.path.abspath(args.spack_opt)
    cache = os.path.abspath(args.cache)

    for path in experiment_dir, outdir, container:
        if not os.path.exists(path):
            sys.exit(f"{path} does not exist.")

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

    # Recursively find experiments
    for experiment_yaml in utils.recursive_find(experiment_dir, "experiment.yaml"):

        # The generator will derive versions, etc. and a matrix of jobs
        gen = ExperimentJobsGenerator(experiment_yaml, outdir)
        matrix += gen.generate_jobs()

    print("Generated %s jobs" % len(matrix))
    print("Shuffling...")
    random.shuffle(matrix)

    for entry in matrix:
        tmpfile = os.path.join(scripts, "%s.sh" % entry["slug"])
        submitfile = os.path.join(scripts, "%s-submit.sh" % entry["slug"])
        outfile = os.path.join(logs_dir, "%s.out" % entry["slug"])
        if not os.path.exists(entry["outdir"]):
            os.makedirs(entry["outdir"])
        templated = template + "\n" + entry["command"]
        submit_templated = submit_template % (cache, spack_opt, container, tmpfile)
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
