# Splice Experiment

This is planning for the [spliced](https://github.com/buildsi/spliced) experiment
that we plan to run for the BUILDSI project. We will use a container base to the largest extent possible.
To see our original manual setup, you can look in [manual](manual).

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


## Running the Experiment

### Clone the repository

It's easiest to get access to the `experiments.yaml` file via a clone, however you
can make your own. It's a yaml file with a single key "experiments" and then a list
of spack package names. E.g.,

```yaml
experiments:
  - caliper
  - swig
  ...
```

If you choose to clone:

```bash
$ git clone https://github.com/buildsi/spliced-experiment
$ cd spliced-experiment
```

### Pull the Container

The container will come with:

 - pyelftools for symbols
 - libabigail
 - abi-laboratory
 - smeagle dependencies (cle)
 - spliced (the main running framework that uses spack)
 
Spack is not provided in the container, as it is intended to be bound. Note that this
container is provided as an automated build for this repository, so you should only need to pull
it down to an HPC system with singularity.

```bash
$ singularity pull docker://ghcr.io/buildsi/spliced-experiment
```

### Experiments

We used a manual approach to derive a list of experiments (just package names in e4s)
that we wanted to run (see [manual](manual)) and put them into the [experiments.yaml](experiments.yaml)
file.

### Prepare Splice Metadata

Since we will submit jobs that run the container, we need to generate our experiments
in separate files. We can use the container for this:

```bash
$ singularity exec --home $PWD spliced-experiment_latest.sif spack python /code/scripts/generate_experiments.py splices/
```

You should not have spack on your path (so it can be found in the container).
Note that home needs to be set to somewhere that isn't actually your home to not interfere with your host configs.
After this run, you can see example splices in [splices](splices).

### Manually Run a Splice

To run a splice you will want to bind:

 - an originally empty directory to install packages to `/spack/opt` (e.g., not a local spack installs)
 - an empty directory to cache data to `/cache`
 - a results directory for results to `/results` (if saving files)

First, generate an example command using an experiment file:

```bash
$ singularity exec --home $PWD spliced-experiment_latest.sif spliced command splices/swig/pcre/pcre/experiment.yaml
```

or with Docker:

```bash
$ docker run -it ghcr.io/buildsi/spliced-experiment spliced command splices/swig/pcre/pcre/experiment.yaml
```

Then you can choose a command, and test running (and printing to the terminal).  Note that we are binding a fresh (empty) install directory with spack installs to the container. This directory should *only* be used for your container, and you should start with it empty. The reason is because paths (from within the container) will be hard-coded there, and you can get erroneous results to have a mixture of both. You'll also need to bind a cache directory to `/cache` - if you don't it will work for Docker but not Singularity (as there will be no write). And we are also binding the original path to itself (so it can be found, e.g., for RPATHs).  Here is Singularity:

```bash
$ mkdir -p cache
$ mkdir -p spack-opt
$ singularity exec --home $PWD --bind $PWD/spack-opt:/spack/opt --bind $PWD/cache:/cache spliced-experiment_latest.sif spliced splice --package swig@1.3.40 --splice pcre --runner spack --replace pcre --experiment experiment
```

and Docker:

```bash
$ docker run -it -v $PWD/spack-opt:/spack/opt ghcr.io/buildsi/spliced-experiment spliced splice --package swig@1.3.40 --splice pcre --runner spack --replace pcre --experiment experiment
```

### Automated Run Splices

The script [submit_jobs.py](scripts/submit_jobs.py) will do exactly that - submit jobs for all your experiments in some subdirectory of `spliced` ensuring we have the correct environment variables, etc. You should provide the input directory (splices), the existing results directory (results) and a path to the container SIF (Singularity).

```bash
$ python scripts/submit_jobs.py ./splices ./results spliced-experiment_latest.sif
```

The above will submit a bunch of jobs for all `experiment.yaml` files it finds under spliced. Note that this variat of experiment.yaml has a splice, replace, and main package (it's not the one in the root here with your main experiment package names). Submission scripts will be written to `$PWD/submit` for you to inspect or re-run.


## Development

If you want to clone this repository, you can develop locally.

```bash
cd /p/vast1/build
git clone https://github.com/buildsi/spliced-experiment
```

### Build the Container

```bash
$ docker build -t ghcr.io/buildsi/spliced-experiment .
```

You can even pull from the docker-deamon after that!

```bash
$ singularity pull docker-daemon:ghcr.io/buildsi/spliced-experiment:latest
```

### Local Spack

If you want to test a local spack against the container, just bind it to `/spack` in the container.
Note that we are currently using an older version of spack that doesn't have as many bugs
that were added with the 0.17 release.

```bash
git clone -b vsoch/db-17-splice-july-25 https://github.com/vsoch/spack
. spack/share/spack/setup-env.sh 
```

Ensure in your default spack config (`spack/etc/spack/defaults/config.yaml`) to set deprecated: true so we download deprecated packages, and that debug is enabled.

```yaml
config:
  deprecated: true
  debug: true
```

