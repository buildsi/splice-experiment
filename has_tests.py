#!/usr/bin/env python3

# A quick script to read in the yaml of experiments and determine if a package
# has tests, and output a subset that do.

import os
import inspect
import sys
import yaml

import spack.package
from spack.spec import Spec

here = os.getcwd()


def read_yaml(filename):
    with open(filename, "r") as fd:
        content = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return content

def write_yaml(filename, content):
    with open(filename, "w") as fd:
        fd.write(yaml.dump(content))

def has_test_method(pkg):
    if not inspect.isclass(pkg):
        return False

    pkg_base = spack.package.PackageBase
    return (issubclass(pkg, pkg_base) and pkg.test != pkg_base.test) or (
        isinstance(pkg, pkg_base) and pkg.test.__func__ != pkg_base.test
    )


def main(yaml_file):
    """
    Given a yaml file with an experiments list, count tests in spack
    """
    if not os.path.exists(yaml_file):
        sys.exit("%s does not exist." % yaml_file)
    experiments = read_yaml(yaml_file)
    has_tests = set()
    for experiment in experiments["experiments"]:
        spec = Spec(experiment)
        if has_test_method(spec.package.__class__):
            has_tests.add(spec.package.name)
    print(
        "%s packages out of %s have tests in %s"
        % (len(has_tests), len(experiments["experiments"]), os.path.basename(yaml_file))
    )
    # Save to file
    dirname = os.path.dirname(yaml_file)
    outfile = os.path.join(dirname, "has_tests.yaml")
    write_yaml(outfile, {"experiments": list(has_tests)})


if __name__ == "__main__":
    yaml_file = os.path.join(here, "experiments", "e4s.yaml")
    if len(sys.argv) > 1:
        yaml_file = sys.argv[1]
    main(yaml_file)
