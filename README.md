# Splice Experiment

This is planning for the [spliced](https://github.com/buildsi/spliced) experiment
that we plan to run for the BUILDSI project. We will use a container base to the largest extent possible.
To see our original manual setup, you can look in [manual](manual), or to read the original
experiment plan and design, see [plan.md](plan.md). Note that @vsoch is currently working on this
locally with docker because there are filesystem issues on HPC.

## Usage

### Singularity and Slurm

Generate all experiments (yaml) and run all splices with Singularity. Make sure spack isn't on your PATH
so it gets picked up in the container!

```bash
$ mkdir -p ./results ./spack-opt ./cache
$ singularity pull docker://ghcr.io/buildsi/spliced-experiment

# Generate splice experiment configs (runs internal to container)
$ singularity exec --containall --home $PWD --bind $PWD/spack-opt:/spack/opt spliced-experiment_latest.sif spack python /code/scripts/generate_experiments.py splices/

# Submit jobs (using configs) to cluster - submission is external to container, runs with container
$ python scripts/submit_jobs.py ./splices spliced-experiment_latest.sif --spack-opt spack-opt --cache cache
```

### Podman and Slurm

```bash
$ mkdir -p ./results ./spack-opt ./cache
$ podman pull ghcr.io/buildsi/spliced-experiment

# Generate splice experiment configs (runs internal to container)
$ podman run -v $(pwd)/spack-opt:/spack/opt -v $(pwd)/splices:/splices ghcr.io/buildsi/spliced-experiment spack python /code/scripts/generate_experiments.py /splices

# Try a single command
$ podman run -v $(pwd)/spack-opt:/spack/opt -v $(pwd)/results:/results -v /tmp/sochat1:/tmp -v $(pwd)/cache:/cache ghcr.io/buildsi/spliced-experiment spack python /usr/local/bin/spliced splice --package swig@fortran --splice pcre --runner spack --replace pcre --experiment experiment

# Submit jobs (using configs) to cluster - submission is external to container, runs with container
$ python scripts/submit_jobs.py ./splices spliced-experiment_latest.sif --spack-opt spack-opt --cache cache --podman
```


The experiment [splices](splices) we generated are included here.

### Preview Underlying Commands

Want to generate commands for a single run, perhaps to test? The following are easy ways to generate commands (for testing):

```bash
# Generate singularity (default) run commands to manually test (with default paths)
$ python scripts/submit_jobs.py ./splices --dry-run

# Generate singularity (default) run commands, with a single command per package (e.g., to time)
$ python scripts/submit_jobs.py ./splices --dry-run --single

# Generate docker run commands to manually test (with default paths)
$ python scripts/submit_jobs.py ./splices --docker --dry-run

# Limit to 10
$ python scripts/submit_jobs.py ./splices --docker --dry-run -N 10

# Custom paths for spack-opt and cache
$ python scripts/submit_jobs.py ./splices --docker --spack-opt ./spack-opt --cache ./cache --dry-run
```

and of course you can shell into any container with the same binds to do the same.


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
$ singularity exec --containall --home $PWD --bind ./spack-opt:/spack/opt spliced-experiment_latest.sif spack python /code/scripts/generate_experiments.py splices/
```

or with Docker:

```bash
$ docker run -v $PWD/cache:/cache -v $PWD/splices:/splices -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/generate_experiments.py /splices/
```

You should not have spack on your path (so it can be found in the container) if you are using Singularity.
Note that home needs to be set to somewhere that isn't actually your home to not interfere with your host configs.
After this run, you can see example splices in [splices](splices).


### Manually Run a Splice

To run a splice you will want to bind:

 - an originally empty directory to install packages to `/spack/opt` (e.g., not a local spack installs)
 - an empty directory to cache data to `/cache`
 - a results directory for results to `/results` (if saving files)

Note that you can also use the commands shown in [Preview Underlying Commands](#preview-underlying-commands) to generate testing commands. First, generate an example command using an experiment file:

```bash
$ singularity exec --containall --home $PWD spliced-experiment_latest.sif spliced command splices/swig/pcre/pcre/experiment.yaml
```

or with Docker:

```bash
$ docker run -it ghcr.io/buildsi/spliced-experiment spliced command splices/swig/pcre/pcre/experiment.yaml
```

Then you can choose a command, and test running (and printing to the terminal).  Note that we are binding a fresh (empty) install directory with spack installs to the container. This directory should *only* be used for your container, and you should start with it empty. The reason is because paths (from within the container) will be hard-coded there, and you can get erroneous results to have a mixture of both. You'll also need to bind a cache directory to `/cache` - if you don't it will work for Docker but not Singularity (as there will be no write). And we are also binding the original path to itself (so it can be found, e.g., for RPATHs).  Here is Singularity:

```bash
$ mkdir -p cache spack-opt
$ singularity exec --containall --home $PWD --bind $PWD/spack-opt:/spack/opt --bind $PWD/cache:/cache spliced-experiment_latest.sif spack python /usr/local/bin/spliced --package swig@1.3.40 --splice pcre --runner spack --replace pcre --experiment experiment
```

and Docker:

```bash
$ docker run -it -v $PWD/spack-opt:/spack/opt ghcr.io/buildsi/spliced-experiment spliced splice --package swig@1.3.40 --splice pcre --runner spack --replace pcre --experiment experiment
```

### Automated Run Splices

The script [submit_jobs.py](scripts/submit_jobs.py) will do exactly that - submit jobs for all your experiments in some subdirectory of `spliced` ensuring we have the correct environment variables, etc. You should provide the input directory (splices), the existing results directory (results) and a path to the container SIF (Singularity).

```bash
$ python scripts/submit_jobs.py ./splices spliced-experiment_latest.sif --spack-opt spack-opt --cache cache
```

The above will submit a bunch of jobs for all `experiment.yaml` files it finds under spliced. Note that this variat of experiment.yaml has a splice, replace, and main package (it's not the one in the root here with your main experiment package names). Submission scripts will be written to `$PWD/submit` for you to inspect or re-run.


### Notes

Conceptually, we are providing a spack install in the container, and only writing the database and libraries installed to our local filesystem to be used as a shared cache. Since an installed package might pull in system libraries, this is why it is essential that you don't bind an actual spack install, and (worse) one that has a mix of already installed things. Also note that the spack in the container is a custom (modified) version that, along with easily printing all versions and other tweaks, runs in debug mode. In practice we found some locking issues on our HPC system and it was helpful to have this verbosity.

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

