#!/usr/bin/env python3

import spack.spec
import sys
import tempfile
import os
import yaml

# You can't use __file__ with spack python
here = os.getcwd()


def read_yaml(filename):
    with open(filename, "r") as fd:
        content = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return content


def write_yaml(filename, content):
    with open(filename, "w") as fd:
        fd.write(yaml.dump(content))


def write_file(filename, content):
    with open(filename, "w") as fd:
        fd.write(content)


template = """
package: %s
splice: %s
replace: %s
"""


def main(yaml_file, outdir):
    packages = read_yaml(yaml_file)["experiments"]

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # For every package in e4s P with tests:
    for package in packages:
        spec = spack.spec.Spec(package)
        spec.concretize()
        # For every dependency of package P, D that is also in e4s:
        for dep in spec.dependencies():

            # "Replace a dependncy with a different version of itself"
            recipe = template % (spec.name, dep.name, dep.name)
            outfile = os.path.join(
                outdir, spec.name, dep.name, dep.name, "experiment.yaml"
            )
            print("Writing %s" % outfile)
            dirname = os.path.dirname(outfile)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            write_file(outfile, recipe)


if __name__ == "__main__":
    yaml_file = os.path.join(here, "experiments.yaml")
    if len(sys.argv) != 2:
        sys.exit("please provide the output directory for experiment yamls.")
    outdir = sys.argv[1]
    main(yaml_file, outdir)
