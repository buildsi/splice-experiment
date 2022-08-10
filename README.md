# Splice Experiment

This is planning for the [spliced](https://github.com/buildsi/spliced) experiment
that we plan to run for the BUILDSI project. We will use a container base to the largest extent possible.
To see our original manual setup, you can look in [manual](manual), or to read the original
experiment plan and design, see [plan.md](plan.md). Note that although the original plan was to run this on HPC, the file-system had significant issues and it was entirely run in GitHub actions. For the interested user,
examples of running scripts are provided for Singularity, Podman, and Docker, in the case you want to do this manually. The actual running of experiments happened in [this repository](https://github.com/buildsi/splice-experiment-runs).

## Setup

### 1. Experiment Derivation

*data from this step is provided here*

To see our first experiment attempt setup, see [attemps.md](attempts.md) where we tried using tests in spack for a ground truth. Ultimately we decided this was not good enough and we would use a set of known libraries with ABI issues (manually defined) in [diffs](diffs).

### 2. Running Experiments

Running experiments is easy, and automated! We use the container build alongside this repostiory with a Github workflow in a separate repository and then can programatically get results. Simply:

1. Ensure this repository is pushed (up to date), as the diffs/splices come from here.
2. Go to [buildsi/splice-experiment-runs Actions](https://github.com/buildsi/splice-experiment-runs/actions)
3. Click on the "Spliced Analysis" workflow, and then "Run Workflow"
4. The name in the box should correspond to the main package and dependency folder to run.

When you are done, you can clone the [artifacts repository](https://github.com/buildsi/splice-experiment-artifacts) to manually update artifacts, or just wait for it to update overnight. The full analysis (with the artifacts as a git submodule) is in [buildsi/splice-experiment-results](https://github.com/buildsi/splice-experiment-results).

## Changelog:

 - version 0.0.1: original version with some tweaks
 - version 0.0.11: updating cle from its master to resolve dependency install bugs [commit](https://github.com/vsoch/cle/commit/b631940d5598e457533866cbc7284123c2c08ef1)
 - version 0.0.12: refactor of spliced to include diff functionality
