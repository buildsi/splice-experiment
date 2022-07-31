#!/usr/bin/env python3

# A quick script to look across spack packages and determine if a subset has tests
# This was run with https://github.com/spack/spack/releases/download/v0.17.3/spack-0.17.3.tar.gz
# Note that 18.x would require you to concretize each to inspect package... yuck.

# 104 packages out of 5969 have tests

import os
import inspect
import sys
import yaml

import spack.package
from spack.spec import Spec
import spack.repo

here = os.getcwd()


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


def main():
    """
    Find packages with tests in spack
    """    
    packages = spack.repo.all_package_names()
    print("Found %s total packages" % len(packages))
    has_tests = set()
    for experiment in packages:

        # Don't include python, typically nothing compiled
        if experiment.startswith('py-'):
            continue
        spec = Spec(experiment)
        if has_test_method(spec.package.__class__):
            print("%s has tests!" % experiment)
            has_tests.add(spec.package.name)

    print("%s packages out of %s have tests" % (len(has_tests), len(packages)))

    # Save to file
    outfile = os.path.join(here, "experiments_with_tests.yaml")
    write_yaml(outfile, {"experiments": list(has_tests)})

if __name__ == "__main__":
    main()
