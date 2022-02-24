#!/usr/bin/env python3

from spliced.client.command import get_package_versions, get_splice_versions
import spliced.experiment
import sys
import tempfile
import os

here = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) != 3:
    sys.exit(
        "Please provide the path to the experiment yaml and an output directory as the only arguments."
    )
experiment_yaml = os.path.abspath(sys.argv[1])
outdir = os.path.abspath(sys.argv[2])

if not os.path.exists(experiment_yaml):
    sys.exit("%s does not exist." % experiment_yaml)

# Generate a base experiment
experiment = spliced.experiment.Experiment()
experiment.load(experiment_yaml)

versions = get_package_versions(experiment.package)
splice_versions = get_splice_versions(experiment)

# Make an output logs directory
logs_dir = os.path.join(here, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# We will build up a matrix of experiments
matrix = []

# Generate list of commands
for version in versions:
    for splice_version in splice_versions:

        # versioned package
        package = "%s@%s" % (experiment.package, version)
        outfile = os.path.join(
            outdir,
            experiment.package,
            version,
            splice_version,
            "%s.json" % experiment.name,
        )
        slug = "%s-%s-%s-%s" % (
            experiment.package,
            version,
            splice_version,
            experiment.name,
        )
        cmd = (
            "spliced splice --package %s --splice %s --runner spack --replace %s --experiment %s --outfile %s"
            % (package, splice_version, experiment.replace, experiment.name, outfile)
        )

        # You can add a custom command here, but we will need to add spack testing when it's ready
        # if experiment.command:
        #    cmd = "%s %s" % (cmd, experiment.command)
        matrix.append(
            {
                "command": cmd,
                "package": package,
                "runner": "spack",
                "splice": experiment.splice,
                "replace": experiment.replace,
                "experiment": experiment.name,
                "outfile": outfile,
                "outdir": os.path.dirname(outfile),
                "slug": slug,
            }
        )

# create scripts directory
scripts = os.path.abspath(os.path.join(here, "scripts"))
if not os.path.exists(scripts):
    os.makedirs(scripts)

template = """#!/bin/bash 

. /p/vast1/build/spack/share/spack/setup-env.sh 

# always build with debug
export SPACK_ADD_DEBUG_FLAGS=true

# add anaconda (or your favorite python install) to the path to install spliced
export PATH=/p/vast1/build/anaconda3/bin:$PATH

"""

for entry in matrix:
    tmpfile = os.path.join(scripts, "%s.sh" % entry["slug"])
    outfile = os.path.join(logs_dir, "%s.out" % entry["slug"])
    errfile = os.path.join(logs_dir, "%s.err" % entry["slug"])
    if not os.path.exists(entry["outdir"]):
        os.makedirs(entry["outdir"])
    templated = template + "\n" + entry["command"]
    with open(tmpfile, "w") as fd:
        fd.writelines(templated)
    os.system("sbatch --time 360 --out=%s --err %s %s" % (outfile, errfile, tmpfile))
    # Just running one to test for now
    sys.exit()
