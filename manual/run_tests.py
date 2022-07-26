#!/usr/bin/env python3

# A quick script to read in the yaml of experiments and run a test given that
# a package has tests.

import os
import inspect
import sys
import yaml
import subprocess
import json
import time

here = os.getcwd()


def read_yaml(filename):
    with open(filename, "r") as fd:
        content = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return content


def run_command(cmd):
    print(" ".join(cmd))
    output = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    t = output.communicate()[0], output.returncode
    output = {"message": t[0], "return_code": t[1]}
    if isinstance(output["message"], bytes):
        output["message"] = output["message"].decode("utf-8")
    return output


def main(yaml_file):
    """
    Given a yaml file with an experiments list, count tests in spack
    """
    if not os.path.exists(yaml_file):
        sys.exit("%s does not exist." % yaml_file)
    experiments = read_yaml(yaml_file)
    outcomes = {}

    for experiment in experiments["experiments"]:

        # I tried SpackCommand here but it didn't work (always froze)
        res = run_command(["spack", "install", experiment])
        if res["return_code"] != 0:
            outcomes[experiment] = {"install": "failure", "reason": res["message"]}
            continue

        outcomes[experiment] = {"install": "success"}
        start = time.time()
        res = run_command(["spack", "test", "run", experiment])
        end = time.time()

        if res["return_code"] != 0:
            outcomes[experiment].update(
                {
                    "test": "failure",
                    "reason": res["message"],
                    "time_seconds": end - start,
                }
            )
        else:
            outcomes[experiment].update(
                {"test": "success", "time_seconds": end - start}
            )

    # Save outcomes to file
    dirname = os.path.dirname(yaml_file)
    with open(os.path.join(dirname, "has_tests_results.json"), "w") as fd:
        fd.write(json.dumps(outcomes, indent=4))

    # Quickly print which had issues
    for name, result in outcomes.items():
        if result["install"] == "failure":
            print("%-20s install failure" % name)
        elif result["test"] == "failure":
            print("%-20s test bug or failure" % name)


if __name__ == "__main__":
    yaml_file = os.path.join(here, "experiments", "has_tests.yaml")
    if len(sys.argv) > 1:
        yaml_file = sys.argv[1]
    main(yaml_file)
