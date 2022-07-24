# Splice Experiment

This is planning for the [spliced](https://github.com/buildsi/spliced) experiment
that we plan to run for the BUILDSI project.

## Pre-requisites

1. We need to finish Smeagle, and add as a tester to [spliced](https://github.com/buildsi/spliced)
2. This experiment will need to be setup to run on slurm / a cluster, meaning installing spack and other dependencies (trying to get the current container base into a working environment).
3. Probably something with [libtree](https://github.com/haampie/libtree) TBA.

## Plan

Once the above are done, here is the plan! 

### Matrix Automated Tests

We will first need to choose a set of compilers appropriate for a scoped analysis (likely related to what Smeagle can parse). The [experiments/e4s.yaml](experiments/e4s.yaml) will be run with a custom Python script
that reads in each e4s package, and:

```bash
For every package in e4s P with tests:
  For every dependency of package P, D that is also in e4s:
    Perform splice of package P and dependency D
```

This means that we also need to know the sample of the e4s packages that have tests.
I wrote a script to do that.

```bash
$ spack python has_tests.py experiments/e4s.yaml
44 packages out of 90 have tests in e4s.yaml
```

This will also generate a file with the subset of packages that have tests:

```bash
$ cat experiments/has_tests.yaml 
experiments:
- swig
...
```

The original spack.yaml for e4s is in [ref](ref) for reference. Finally, once you  have
this list, you can do a run on your host to determine which tests might be broken (my first
run 14/44 failed, or a little less than 1/3, where 1/3 is about half of the libraries in the e4s set.

```bash
$ python run_tests.py
qthreads             test bug or failure
hypre                test bug or failure
superlu              test bug or failure
kokkos               test bug or failure
bolt                 test bug or failure
parsec               test bug or failure
superlu-dist         test bug or failure
heffte               test bug or failure
aml                  install failure
arborx               test bug or failure
tasmanian            test bug or failure
slepc                test bug or failure
ginkgo               test bug or failure
caliper              test bug or failure
```

For full details and error messages you can see [experiments/has_tests_results.json](experiments/has_tests_results.json).


### Manual Tests

Since we can't splice in things that aren't dependencies in spack (and we need the tests above) we also need a manual approach
that picks/chooses some manual cases that we know will cause issue (e.g. mpich and openmpi) to run those.
We will want to do these "by hand" and perhaps run a manual experiment (not developed yet in spliced but should be fairly
easy to do) to run the predictions without needing to spack install them.


## Running the Experiment

### A Test Run

Note that you can do this *after* the setup has been done in [detailed instructions](#detailed-instructions) below.

```bash
# Go to our build space
cd /p/vast1/build 

# I need to do this because I alias python3 to python (you might not)
unalias python

# ABI Laboratory container
export SPLICED_ABILAB_CONTAINER=/p/vast1/build/abi-laboratory-docker_latest.sif

# Source the spack in build
. spack/share/spack/setup-env.sh 

# always build with debug (this is in template script too)
export SPACK_ADD_DEBUG_FLAGS=true

# add anaconda to the path (where spliced, symbolator are installed)
export PATH=/p/vast1/build/anaconda3/bin:$PATH

# Add smeagle facts cache (in a place that will get big)
export SPLICED_SMEAGLE_CACHE_DIR=/p/vast1/build/smeagle-cache

# double check you are using the right spack and python
which spack
# /p/vast1/build/spack/bin/spack
which python
# /p/vast1/build/anaconda3/bin/python

# get a NOOOOODE
salloc -N 1

# cd into the experiment directory where we have configs
cd spliced-experiment

# Here is how I generate commands (printed to the terminal) and you can use any experiment config in splices/
spliced command splices/swig/pcre/pcre/experiment.yaml

# Here is one I chose from the list printed
spliced splice --package swig@master --splice pcre --runner spack --replace pcre --experiment experiment
# You can set an --outfile to save output, but for testing it's fine to just watch the terminal!
```

### Detailed Instructions

Let's clone the experiment repository to get the examples and scripts.
We have space in `/p/vast1/build`

```bash
cd /p/vast1/build
git clone https://github.com/buildsi/spliced-experiment
```

Let's install anaconda to avoid pain.

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
chmod +x Anaconda3-2022.05-Linux-x86_64.sh
./Anaconda3-2022.05-Linux-x86_64.sh -p /p/vast1/build/anaconda3
```

And we need spack.

```bash
git clone -b vsoch/vsoch/db-17-splice-mar-18 https://github.com/vsoch/spack
. spack/share/spack/setup-env.sh 

# always build with debug (this is in template script too)
export SPACK_ADD_DEBUG_FLAGS=true

# add anaconda (or your favorite python install) to the path to install spliced
export PATH=/p/vast1/build/anaconda3/bin:$PATH
spack compiler find
```

Ensure in your default spack config (`spack/etc/spack/defaults/config.yaml`) to set deprecated: true so we download deprecated packages,
and that debug is enabled.

```yaml
config:
  deprecated: true
  debug: true
```

Note that libabigail with gcc 10.2.0 is going to fail, so we need to use a different
compiler and install before running anything.

```bash
$ module load gcc/8.3.1
$ spack install libabigail%gcc@8.3.1
```

Install [spliced](https://github.com/buildsi/spliced) and [symbolator](https://github.com/buildsi/symbolator)

```bash
pip install spliced symbolator-python
```

And then cle:

```bash
git clone https://github.com/vsoch/cle

# archinfo, pyvex, pyelftools, then cle
pip install wheel
pip install git+https://github.com/angr/archinfo
pip install git+https://github.com/angr/pyvex
pip install git+https://github.com/eliben/pyelftools
pip install .
```

You can see example splices in [splices](splices) and we are going to be generating them programatically
based on tests we have.

## Containers

One of our predictors (the ABI laboratory) is easiest to use from a container!
Pull the container with singularity:

```bash
$ singularity pull docker://ghcr.io/buildsi/abi-laboratory-docker
```

And ensure you export the environment variable for the predictor to find.

```bash
$ export SPLICED_ABILAB_CONTAINER=/p/vast1/build/abi-laboratory-docker_latest.sif
```

## Generating experiments

To generate new experiment files we can do the following:

```bash
$ mkdir -p splices
$ spack python generate_experiments.py splices/
```

Note that @vsoch has probably already run this if there is a "splices" directory in the
repository. Then you can have spliced generate the commands for you.  Here is an example
to run on your own to see:

```bash
spliced command splices/swig/pcre/pcre/experiment.yaml
```

Take a look at the commands generated above if you are interested. But let's do this in Python. Make a root output directory alongside spack

```bash
$ mkdir -p results
```

Finally, export a cache directory for Smeagle (so we only derive facts once)

```bash
export SPLICED_SMEAGLE_CACHE_DIR=/p/vast1/build/smeagle-cache
```

The script [submit_jobs.py](submit_jobs.py) will do exactly that - submit jobs ensuring we have 
the correct environment variables, etc.

**important** I've hard coded the template for the submission script at the bottom of that script, please
change this to be where your spack install is, etc. It's hard coded for mine because *reasons*.

The above will submit a bunch of jobs for all versions of the input parameters on the cluster,
and keep scripts in `$PWD/scripts`

```bash
                        # experiment                           # output directory
$ python submit_jobs.py splices/swig/pcre/pcre/experiment.yaml results
```
