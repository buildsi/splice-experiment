#!/usr/bin/env python3

# A quick script to read in the yaml of experiments and determine if a package
# has tests, and output a subset that do.

import os
import yaml

from spack.spec import Spec

here = os.getcwd()

def read_yaml(filename):
    with open(filename, 'r') as fd:
        content = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return content

def main():
    # Read in e4s packages
    experiments = read_yaml(os.path.join(here, "experiments", "e4s.yaml"))
    for experiment in experiments['experiments']:
        spec = Spec(experiment)

        # TODO how do we determine this? This doesn't seem to work
        if spec.package.test_suite is not None:
            print(spec)
        
    import IPython
    IPython.embed()

if __name__ == "__main__":
    main()
