## Version 0.0.11

### 1. Experiment Generation

Starting from the repository cloned, first we generated [experiments_with_tests.yaml](experiments_with_tests.yaml). This was run with a previous (17.x) version of spack, as concetization wasn't required to inspect the underlying package.

```bash
cd /tmp
wget https://github.com/spack/spack/releases/download/v0.17.3/spack-0.17.3.tar.gz
tar -xzvf spack-0.17.3.tar.gz
export PATH=/tmp/spack-0.17.3/bin:$PATH
```

After the above, the spack from that install should be on the path, and you can run the command with spack
python to generate the [experiments_with_tests.yaml](experiments_with_tests.yaml) file.

```bash
$ spack python scripts/derive_experiments.py
```

Across spack, when we remove Python libraries, there are unfortunately only 104 with tests.

### 2. Filtering

*data from this step is provided here*

Since @vsoch was going to run this in GitHub actions, she wanted to ensure she only used workers for packages that would actually build. To do this, she used the same underlying runner container (bound to a common install directory) and manually tested the base installs (what spack installs by default) to filter down to a set of experiments that would build. In addition, she also removed experiments that didn't have any binaries in bin or lib.
The final set of experiments are in [experiments.yaml](experiments.yaml), and they are separated into e4s and non-e4s packages (the latter set was too small for the entire study). You can see a log of her work in [manual-runs.md](manual-runs.md). If you want to use the container interactively to do similar, you can do:

```bash
$ mkdir -p spack-opt
$ docker run -it -v $PWD/spack-opt:/spack/opt ghcr.io/buildsi/spliced-experiment
```

Binding spack-opt allows for re-use (and faster testing).

### 3. Splice Experiment Generation

*data from this step is provided here*

At this point we want to take the experiments.yaml and generate [splices](splices).
Here is how to generate that directory:

```bash
$ docker run -v $PWD/splices:/splices -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/generate_experiments.py /splices/
```

Note that the experiments.yaml is used inside the container at `/code/experiments.yaml`, so if you change it you will need to bind a file explicitly there (or rebuild the container locally). In addition, for dependencies with many versions (and too many to run within 6 hours) @vsoch selected a consistent range (e.g., Python)
and defined the `splice_versions` of the experiment.yaml in splices. This is so the run would be reasonable to do on GitHub actions.

To see commands that are possible using the containers for other environments (but not used here) see [commands.md](commands.md)
