# Does it Build?

Welcome to the new game of...

> Does it build?

This is a manual test of installing the main packages (to be spliced) - if this fails, there is no point attempting them in the experiment. Spack MUST build and splice them to get any kind of result. From the below, I've derived the following list of packages we can run/test in GitHub actions. I'm also linking to the runs that were used for the experiment.

 - [x] qthreads/numactl ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2762890515))
 - [x] hdf5/pkgconf ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2764243645))
 - [x] hdf5/zlib ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2764243977))
 - [x] raja/blt ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2762946012))
 - [x] raja/camp ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2762946312))
 - [x] bolt/argobots ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2769095079)) only successful for main
 - [x] bolt/autoconf ([run](https://github.com/buildsi/splice-experiment-runs/runs/7597830173?check_suite_focus=true)) only successful for main
 - [x] darshan-util/autoconf ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767479049)) (we have a few results, some versions failed)
 - [x] darshan-util/libtool ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767481780))
 - [x] darshan-util/m4 ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767482219))
 - [x] darshan-util/zlib ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767482631))
 - [x] swig/pcre ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767484624))
 - [x] swig/pkgconf([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767485056))

Not e4s, but have tests (and were added)

 - [x] binutils/diffutils ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2770405790))
 - [x] binutils/gettext ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2770713059))
 - [x] binutils/zlib ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2770860947))
 - [x] cget/python ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771126935))

 - [x] biobambam2/autoconf ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771652502))
 - [x] biobambam2/libmaus2 ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771645367))
 - [x] biobambam2/libtool ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771645624))
 - [x] biobambam2/m4 ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771650932))

 - [x] dssp/autoconf ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771130783))
 - [x] dssp/boost ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771131926))
 - [x] dssp/libtool ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771133304))
 - [x] dssp/m4 ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771133485))

 - [x] emacs/libjpeg-turbo ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2772785270))
 - [x] emacs/libxml2 ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2772787764))
 - [x] emacs/ncurses ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2772790365))
 - [ ] emacs/pcre ([run]())
 - [ ] emacs/pkgconf ([run]())
 - [ ] emacs/zlib ([run]())

 - [x] falcon/pacbio-daligner ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2772792981))
 - [ ] falcon/pacbio-damasker ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2772794886))
 - [ ] falcon/pacbio-dazz-db ([run]())
 - [ ] falcon/pacbio-dextractor ([run]())
 - [ ] falcon/python ([run]())
 - [x] formetis/metis ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2772800557))

 - [ ] gdal/brunsli ([run]())
 - [ ] gdal/expat ([run]())
 - [ ] gdal/geos ([run]())
 - [ ] gdal/json-c ([run]())
 - [ ] gdal/lerc ([run]())
 - [ ] gdal/libgeotiff ([run]())
 - [ ] gdal/libjpeg-turbo ([run]())
 - [ ] gdal/libpng ([run]())
 - [ ] gdal/libtiff ([run]())
 - [ ] gdal/ninja ([run]())
 - [ ] gdal/pkgconf ([run]())
 - [ ] gdal/proj ([run]())
 - [ ] gdal/qhull ([run]())
 - [ ] gdal/sqlite ([run]())
 - [ ] gdal/zlib ([run]())

 - [x] m4/diffutils ([run]())
 - [x] m4/libsigsegv ([run]())

 - [ ] genesis/openblas ([run]())
 - [ ] genesis/openmpi ([run]())

 - [x] libxml2/libiconv ([run]())
 - [ ] libxml2/pkgconf ([run]())
 - [x] libxml2/xz ([run]())
 - [ ] libxml2/zlib ([run]())
 - [ ] mercurial/python ([run]())
 - [x] meson/ninja  ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2772810403))
 - [ ] meson/python  ([run]())

 - [ ] minimap2/python ([run]())
 - [ ] minimap2/zlib ([run]())
 - [ ] mptensor/openblas ([run]())

 - [ ] openmpi/hwloc ([run]())
 - [ ] openmpi/numactl ([run]())
 - [ ] openmpi/openssh ([run]())
 - [ ] openmpi/perl ([run]())
 - [ ] openmpi/pkgconf ([run]())
 - [ ] openmpi/pmix ([run]())
 - [ ] openmpi/zlib ([run]())

 - [ ] parallel-netcdf/m4 ([run]())
 - [ ] parallel-netcdf/openmpi ([run]())
 - [ ] parallel-netcdf/perl ([run]())
 
 - [ ] perl/berkeley-db ([run]())
 - [ ] perl/bzip2 ([run]())
 - [ ] perl/gdbm ([run]())
 - [ ] perl/zlib ([run]())
 
 - [ ] python/bzip2 ([run]())
 - [ ] python/expat ([run]())
 - [ ] python/gdbm ([run]())
 - [ ] python/gettext ([run]())
 - [ ] python/libffi ([run]())
 - [ ] python/ncurses ([run]())
 - [ ] python/openssl ([run]())
 - [ ] python/pkgconf ([run]())
 - [ ] python/readline ([run]())
 - [ ] python/sqlite ([run]())
 - [ ] python/util-linux-uuid ([run]())
 - [ ] python/xz ([run]())
 - [ ] python/zlib ([run]())

 - [ ] tk/libx11 ([run]())
 - [ ] tk/libxft ([run]())
 - [ ] tk/libxscrnsaver ([run]())
 - [ ] tk/tcl ([run]())
 
 - [ ] uftrace/capstone  ([run]())
 - [ ] uftrace/elfutils  ([run]())
 - [ ] uftrace/libunwind  ([run]())
 - [ ] uftrace/lua-luajit  ([run]())
 - [ ] uftrace/ncurses  ([run]())
 - [ ] uftrace/pkgconf  ([run]())
 - [ ] uftrace/python  ([run]())
 
 - [ ] pinentry/libassuan ([run]())
 - [ ] pinentry/libgpg-error ([run]())
 - [ ] sqlite/readline ([run]())
 - [ ] sqlite/zlib ([run]())
 
 - [ ] umpire/blt ([run]())
 - [ ] umpire/blt ([run]())
 - [ ] umpire/camp ([run]())
 
 - [ ] warpx/fftw ([run]())
 - [ ] warpx/openmpi ([run]())
 - [ ] warpx/openpmd-api ([run]())
 - [ ] warpx/pkgconf ([run]())

These were run with a smaller set of dependency versions (to fit in GH-actions):

 - [x] arborx/kokkos ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2770335432))
 - [x] upcxx/python ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2770326508))


The following packages were either attempted or decided to not be used:

 - [ ] legion/zlib ([run](https://github.com/buildsi/splice-experiment-runs/runs/7592992926?check_suite_focus=true)) is Python and doesn't have any libs/binaries that are ELF.
 - [ ] superlu/openblas ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767052014))
 - [ ] bolt/automake ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767908491)) automake won't work, something about the container
 - [ ] darshan-util/automake ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2767480400)) we can't iterate over automake, error that aclocal file missing (cannot reproduce locally).
 - [ ] cmake/ncurses ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771128292))
 - [ ] cmake/openssl ([run](https://github.com/buildsi/splice-experiment-runs/actions/runs/2771128599)) these timed out.


A checkbox means we have run -> artifacts -> results. Here are additional libraries with tests we can use:

Testing install of additional packages:


 - alps: failed
 - busco: failed
 - callflow: failed 
 - cpmd: manual download required
 - darshan-runtime: failed
 - eigenexa: failed 
 - gatetools: needs llvm, too much for gh-actions
 - hdf: failed
 - ibm-databroker: failed
 - kitty: failed
 - magma: killed
 - mpich: yaksa too big
 - mxnet: too long to build
 - n2p2: failed 
 - omega-h: requires trillinos, nope
 - nrm: failed
 - openrasmol: failed
 - phylice: boost somewhere...
 - povray: boost somewhere...
 - timemory: has submodules that failed
 - tix: fail


### strumpack: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package strumpack@3.1.1 --splice zfp --runner spack --replace zfp --experiment strumpack --outfile /results/strumpack/3.1.1/zfp/experiment.json

==> Error: OSError: No such file or directory: '/tmp/root/spack-stage/spack-stage-strumpack-3.1.1-x4jojz2yzdhqsnq6lderc4vf72g5nch4/spack-src/examples/data'

/spack/lib/spack/spack/package_base.py:1929, in cache_extra_test_sources:
       1926            if os.path.isdir(src_path):
       1927                fsys.install_tree(src_path, dest_path)
       1928            else:
  >>   1929                fsys.mkdirp(os.path.dirname(dest_path))
       1930                fsys.copy(src_path, dest_path)
```


### hpctoolkit: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package hpctoolkit@2019.12.28 --splice papi --runner spack --replace papi@master --experiment hpctoolkit --outfile /results/hpctoolkit/2019.12.28/papi/experiment.json

==> [2022-07-28-18:39:32.583412, 259915] No patches needed for gotcha
==> [2022-07-28-18:39:32.583512, 259915] 259915: gotcha: Building gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb [CMakePackage]
==> [2022-07-28-18:39:32.583806, 259915] write locking [5967684752025944315:1]: timeout 60 sec
==> [2022-07-28-18:39:32.583922, 259915] WRITE LOCK (spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb): /tmp/root/spack-stage/.lock[5967684752025944315:1] [Acquired at 18:39:32.583892] 
==> [2022-07-28-18:39:32.597318, 259915] 259915: gotcha: Executing phase: 'cmake'
==> [2022-07-28-18:39:32.988257, 259915] 259915: gotcha: Executing phase: 'build'
==> [2022-07-28-18:39:33.580564, 259915] WRITE LOCK (spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb): /tmp/root/spack-stage/.lock[5967684752025944315:1] [Released at 18:39:33.580527] 
==> [2022-07-28-18:39:33.601867, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8'

9 errors found in build log:
     124    cd /tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spac
            k-build-mwysjpl && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-p
            mpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_depends "Unix Makefiles" /tmp/root/s
            pack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spack-src /tmp/roo
            t/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spack-src/src/e
            xample/autotee /tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlq
            utbeevb/spack-build-mwysjpl /tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap
            5sdwqj5qflhlqutbeevb/spack-build-mwysjpl/src/example/autotee /tmp/root/spack-stage/spac
            k-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spack-build-mwysjpl/src/example/a
            utotee/CMakeFiles/autotee_test.dir/DependInfo.cmake --color=
     125    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap
            5sdwqj5qflhlqutbeevb/spack-build-mwysjpl'
     126    make  -f src/example/autotee/CMakeFiles/autotee_test.dir/build.make src/example/autotee
            /CMakeFiles/autotee_test.dir/build
     127    make[2]: Entering directory '/tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7aha
            p5sdwqj5qflhlqutbeevb/spack-build-mwysjpl'
     128    [ 94%] Building C object src/example/autotee/CMakeFiles/autotee_test.dir/test_autotee.c
            .o
     129    cd /tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spac
            k-build-mwysjpl/src/example/autotee && /spack/lib/spack/env/gcc/gcc  -I/tmp/root/spack-
            stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spack-src/include -I/tm
            p/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spack-src/
            src -O2 -g -DNDEBUG -MD -MT src/example/autotee/CMakeFiles/autotee_test.dir/test_autote
            e.c.o -MF CMakeFiles/autotee_test.dir/test_autotee.c.o.d -o CMakeFiles/autotee_test.dir
            /test_autotee.c.o -c /tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5
            qflhlqutbeevb/spack-src/src/example/autotee/test_autotee.c
  >> 130    /usr/bin/ld: ../../libgotcha.so.2.0.2: undefined reference to `_dl_sym'
  >> 131    collect2: error: ld returned 1 exit status
  >> 132    make[2]: *** [src/example/minimal/CMakeFiles/symb_look.dir/build.make:102: src/example/
            minimal/symb_look] Error 1
     133    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap
            5sdwqj5qflhlqutbeevb/spack-build-mwysjpl'
  >> 134    make[1]: *** [CMakeFiles/Makefile2:279: src/example/minimal/CMakeFiles/symb_look.dir/al
            l] Error 2
     135    make[1]: *** Waiting for unfinished jobs....
     136    [100%] Linking C executable autotee_test
     137    cd /tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spac
            k-build-mwysjpl/src/example/autotee && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-1
            1.2.0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMak
            eFiles/autotee_test.dir/link.txt --verbose=1
     138    /spack/lib/spack/env/gcc/gcc -O2 -g -DNDEBUG -rdynamic CMakeFiles/autotee_test.dir/test
            _autotee.c.o -o autotee_test  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-gotcha-1.0.3
            -mwysjpl7ahap5sdwqj5qflhlqutbeevb/spack-build-mwysjpl/src/example/autotee:/tmp/root/spa
            ck-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap5sdwqj5qflhlqutbeevb/spack-build-mwysjpl/
            src libautotee.so ../../libgotcha.so.2.0.2
  >> 139    /usr/bin/ld: ../../libgotcha.so.2.0.2: undefined reference to `_dl_sym'
  >> 140    collect2: error: ld returned 1 exit status
  >> 141    make[2]: *** [src/example/autotee/CMakeFiles/autotee_test.dir/build.make:102: src/examp
            le/autotee/autotee_test] Error 1
     142    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap
            5sdwqj5qflhlqutbeevb/spack-build-mwysjpl'
  >> 143    make[1]: *** [CMakeFiles/Makefile2:226: src/example/autotee/CMakeFiles/autotee_test.dir
            /all] Error 2
     144    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-gotcha-1.0.3-mwysjpl7ahap
            5sdwqj5qflhlqutbeevb/spack-build-mwysjpl'
  >> 145    make: *** [Makefile:139: all] Error 2
```



### py-warpx: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package py-warpx@21.04 --splice python@3.8.1 --runner spack --replace python --experiment py-warpx --outfile /results/py-warpx/21.04/python/experiment.json

    '/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/python-3.9.13-a7owmregm4a2ef43uk4x6eyjngeqymej/bin/python3.9' '-m' 'pip' '-vvv' '--no-input' '--no-cache-dir' '--disable-pip-version-check' 'install' '--no-deps' '--ignore-installed' '--no-build-isolation' '--no-warn-script-location' '--no-index' '--prefix=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/py-scipy-1.8.1-3ikxtmm2pwmdbqn4gdsb2463c2lwlpaa' '.'

2 errors found in build log:
     11    Created temporary directory: /tmp/pip-install-whsazj3m
     12    Processing /tmp/root/spack-stage/spack-stage-py-scipy-1.8.1-3ikxtmm2pwmdbqn4gdsb2463c2lw
           lpaa/spack-src
     13      Added file:///tmp/root/spack-stage/spack-stage-py-scipy-1.8.1-3ikxtmm2pwmdbqn4gdsb2463
           c2lwlpaa/spack-src to build tracker '/tmp/pip-build-tracker-5cpxj4mi'
     14      Created temporary directory: /tmp/pip-modern-metadata-as5z10nq
     15      Preparing metadata (pyproject.toml): started
     16      Running command Preparing metadata (pyproject.toml)
  >> 17    setup.py:486: UserWarning: Unrecognized setuptools command ('dist_info --egg-base /tmp/p
           ip-modern-metadata-as5z10nq'), proceeding with generating Cython sources and expanding t
           emplates
     18        warnings.warn("Unrecognized setuptools command ('{}'), proceeding with "
     19      Error: 'numpy' must be installed before running the build.
     20    
     21      error: subprocess-exited-with-error
     22    
     23      × Preparing metadata (pyproject.toml) did not run successfully.

     ...

     25      ╰─> See above for output.
     26    
     27      note: This error originates from a subprocess, and is likely not a problem with pip.
     28      full command: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/python-3.9.13-a7ow
           mregm4a2ef43uk4x6eyjngeqymej/bin/python3.9 /spack/opt/spack/linux-ubuntu22.04-skylake/gc
           c-11.2.0/py-pip-22.1.2-gerucbbxb4idfmxo4ytzhuoylqdodiyp/lib/python3.9/site-packages/pip/
           _vendor/pep517/in_process/_in_process.py prepare_metadata_for_build_wheel /tmp/tmpys1dje
           eh
     29      cwd: /tmp/root/spack-stage/spack-stage-py-scipy-1.8.1-3ikxtmm2pwmdbqn4gdsb2463c2lwlpaa
           /spack-src
     30      Preparing metadata (pyproject.toml): finished with status 'error'
  >> 31    error: metadata-generation-failed
     32    
     33    × Encountered error while generating package metadata.
     34    ╰─> See above for output.
     35    
     36    note: This is an issue with the package mentioned above, not pip.
     37    hint: See above for details.
```


### papyrus: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package papyrus@1.0.0 --splice openmpi --runner spack --replace openmpi --experiment papyrus --outfile /results/papyrus/1.0.0/openmpi/experiment.json

==> openmpi: Executing phase: 'autoreconf'
==> openmpi: Executing phase: 'configure'
==> Error: ProcessError: Command exited with status 1:
    '/tmp/root/spack-stage/spack-stage-openmpi-main-ccf6ioemc73y22b4r4ney7qmpyn2b34i/spack-src/configure' '--prefix=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-main-ccf6ioemc73y22b4r4ney7qmpyn2b34i' '--enable-shared' '--disable-silent-rules' '--disable-builtin-atomics' '--enable-static' '--enable-mpi1-compatibility' '--without-psm2' '--without-mxm' '--without-psm' '--without-ucx' '--without-fca' '--without-knem' '--without-hcoll' '--without-ofi' '--without-xpmem' '--without-cma' '--without-verbs' '--without-cray-xpmem' '--without-loadleveler' '--without-alps' '--without-sge' '--without-lsf' '--without-slurm' '--without-tm' '--disable-memchecker' '--with-libevent=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libevent-2.1.12-eikbakv4aqqnd2i5a7rminoccl2rw6a6' '--with-zlib=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7sovaylq' '--with-hwloc=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-2.7.1-i5ayu7korr7gkh6qtnglfrh7uii2a2eo' '--disable-java' '--disable-mpi-java' '--with-gpfs=no' '--without-cuda' '--enable-wrapper-rpath' '--disable-wrapper-runpath'

29 errors found in build log:
     576     libtoolize: copying file './config/ltsugar.m4'
     577     libtoolize: copying file './config/ltversion.m4'
     578     libtoolize: copying file './config/lt~obsolete.m4'
     579     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoconf --include=config --force --warnings=a
             ll,no-obsolete,no-override
     580     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoheader --include=config --force --warnings
             =all,no-obsolete,no-override
     581     autoreconf: running: automake --add-missing --copy --force-missing --warnings=all,no-o
             bsolete,no-override
  >> 582     configure.ac:211: installing './config/ar-lib'
  >> 583     configure.ac:113: installing './config/compile'
  >> 584     configure.ac:98: installing './config/config.guess'
  >> 585     configure.ac:98: installing './config/config.sub'
  >> 586     configure.ac:101: installing './config/install-sh'
  >> 587     configure.ac:101: installing './config/missing'
     588     examples/Makefile.am: installing './config/depcomp'
     589     configure.ac: installing './config/ylwrap'
     590     parallel-tests: installing './config/test-driver'
     591     autoreconf: Leaving directory `.'
     592     === Patching PGI compiler version numbers in ltmain.sh
     593     === Patching "-pthread" option for NAG compiler in ltmain.sh

     ...

     783     libtoolize: copying file 'config/ltsugar.m4'
     784     libtoolize: copying file 'config/ltversion.m4'
     785     libtoolize: copying file 'config/lt~obsolete.m4'
     786     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoconf --include=config --force --warnings=a
             ll,no-obsolete,no-override
     787     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoheader --include=config --force --warnings
             =all,no-obsolete,no-override
     788     autoreconf: running: automake --add-missing --copy --force-missing --warnings=all,no-o
             bsolete,no-override
  >> 789     configure.ac:118: installing 'config/compile'
  >> 790     configure.ac:105: installing 'config/config.guess'
  >> 791     configure.ac:105: installing 'config/config.sub'
  >> 792     configure.ac:132: installing 'config/install-sh'
  >> 793     configure.ac:132: installing 'config/missing'
     794     src/Makefile.am: installing 'config/depcomp'
     795     configure.ac: installing 'config/ylwrap'
     796     autoreconf: Leaving directory `.'
     797     === Patching PGI compiler version numbers in ltmain.sh
     798     === Patching "-pthread" option for NAG compiler in ltmain.sh
     799     

     ...

     835     libtoolize: copying file 'confdb/ltsugar.m4'
     836     libtoolize: copying file 'confdb/ltversion.m4'
     837     libtoolize: copying file 'confdb/lt~obsolete.m4'
     838     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoconf --include=confdb --force
     839     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoheader --include=confdb --force
     840     autoreconf: running: automake --add-missing --copy --force-missing
  >> 841     configure.ac:50: installing 'confdb/ar-lib'
  >> 842     configure.ac:42: installing 'confdb/compile'
  >> 843     configure.ac:52: installing 'confdb/config.guess'
  >> 844     configure.ac:52: installing 'confdb/config.sub'
  >> 845     configure.ac:38: installing 'confdb/install-sh'
  >> 846     configure.ac:38: installing 'confdb/missing'
     847     Makefile.am: installing 'confdb/depcomp'
     848     autoreconf: Leaving directory `.'
     849     === running autoreconf in 'mpl' ===
     850     autoreconf: Entering directory `.'
     851     autoreconf: configure.ac: not using Gettext
     852     autoreconf: running: aclocal --force -I confdb

     ...

     860     libtoolize: copying file 'confdb/ltsugar.m4'
     861     libtoolize: copying file 'confdb/ltversion.m4'
     862     libtoolize: copying file 'confdb/lt~obsolete.m4'
     863     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoconf --force
     864     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoheader --force
     865     autoreconf: running: automake --add-missing --copy --force-missing
  >> 866     configure.ac:24: installing 'confdb/ar-lib'
  >> 867     configure.ac:18: installing 'confdb/compile'
  >> 868     configure.ac:30: installing 'confdb/config.guess'
  >> 869     configure.ac:30: installing 'confdb/config.sub'
  >> 870     configure.ac:15: installing 'confdb/install-sh'
  >> 871     configure.ac:15: installing 'confdb/missing'
     872     Makefile.am: installing 'confdb/depcomp'
     873     parallel-tests: installing 'confdb/test-driver'
     874     autoreconf: Leaving directory `.'
     875         Patching configure for Libtool PGI 10 fortran compiler name
     876         Patching configure for Libtool PGI version number regexps
     877         Patching configure for flang Fortran ()

     ...

     909     libtoolize: copying file 'config/ltsugar.m4'
     910     libtoolize: copying file 'config/ltversion.m4'
     911     libtoolize: copying file 'config/lt~obsolete.m4'
     912     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoconf --include=config --force --warnings=a
             ll,no-obsolete,no-override
     913     autoreconf: running: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/autoconf-2.
             69-l4m7iqwqvujolsojtwrvktux4dcoa2ad/bin/autoheader --include=config --force --warnings
             =all,no-obsolete,no-override
     914     autoreconf: running: automake --add-missing --copy --force-missing --warnings=all,no-o
             bsolete,no-override
  >> 915     configure.ac:367: installing 'config/compile'
  >> 916     configure.ac:96: installing 'config/config.guess'
  >> 917     configure.ac:96: installing 'config/config.sub'
  >> 918     configure.ac:108: installing 'config/install-sh'
  >> 919     configure.ac:108: installing 'config/missing'
     920     3rd-party/treematch/Makefile.am: installing 'config/depcomp'
     921     parallel-tests: installing 'config/test-driver'
     922     configure.ac: installing 'config/ylwrap'
     923     autoreconf: Leaving directory `.'
     924     === Patching PGI compiler version numbers in ltmain.sh
     925     === Patching "-pthread" option for NAG compiler in ltmain.sh

     ...

     1807    checking for flex... no
     1808    checking for lex... no
     1809    configure: WARNING: *** Could not find Flex on your system.
     1810    configure: WARNING: *** Flex is required for developer builds of Open MPI.
     1811    configure: WARNING: *** Other versions of Lex are not supported.
     1812    configure: WARNING: *** NOTE: If you are building a tarball downloaded from www.open-m
             pi.org, you do not need Flex
  >> 1813    configure: error: Cannot continue

See build log for details:
  /tmp/root/spack-stage/spack-stage-openmpi-main-ccf6ioemc73y22b4r4ney7qmpyn2b34i/spack-build-out.txt

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/spliced/experiment/spack.py", line 121, in do_install
    spec.package.do_install(force=True)
  File "/spack/lib/spack/spack/package_base.py", line 1905, in do_install
    builder.install()
  File "/spack/lib/spack/spack/installer.py", line 1699, in install
    self._install_task(task)
  File "/spack/lib/spack/spack/installer.py", line 1233, in _install_task
    spack.build_environment.start_build_process(
  File "/spack/lib/spack/spack/build_environment.py", line 1200, in start_build_process
    raise child_result
spack.build_environment.ChildError: ProcessError: Command exited with status 1:
    '/tmp/root/spack-stage/spack-stage-openmpi-main-ccf6ioemc73y22b4r4ney7qmpyn2b34i/spack-src/configure' '--prefix=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-main-ccf6ioemc73y22b4r4ney7qmpyn2b34i' '--enable-shared' '--disable-silent-rules' '--disable-builtin-atomics' '--enable-static' '--enable-mpi1-compatibility' '--without-psm2' '--without-mxm' '--without-psm' '--without-ucx' '--without-fca' '--without-knem' '--without-hcoll' '--without-ofi' '--without-xpmem' '--without-cma' '--without-verbs' '--without-cray-xpmem' '--without-loadleveler' '--without-alps' '--without-sge' '--without-lsf' '--without-slurm' '--without-tm' '--disable-memchecker' '--with-libevent=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libevent-2.1.12-eikbakv4aqqnd2i5a7rminoccl2rw6a6' '--with-zlib=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7sovaylq' '--with-hwloc=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-2.7.1-i5ayu7korr7gkh6qtnglfrh7uii2a2eo' '--disable-java' '--disable-mpi-java' '--with-gpfs=no' '--without-cuda' '--enable-wrapper-rpath' '--disable-wrapper-runpath'
```

Tested a second time - more mpi bugs so we cannot build original.

### openpmd-api: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package openpmd-api@0.11.1 --splice adios2 --runner spack --replace adios2 --experiment openpmd-api --outfile /results/openpmd-api/0.11.1/adios2/experiment.json

==> Error: ProcessError: Command exited with status 1:
    'cmake' '-G' 'Unix Makefiles' '-DCMAKE_INSTALL_PREFIX:STRING=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openpmd-api-0.11.1-fhdp7nfpzfaaz52o5ilhk2bgfyvgsvmj' '-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo' '-DBUILD_TESTING:BOOL=OFF' '-DCMAKE_INTERPROCEDURAL_OPTIMIZATION:BOOL=OFF' '-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON' '-DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=ON' '-DCMAKE_INSTALL_RPATH:STRING=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openpmd-api-0.11.1-fhdp7nfpzfaaz52o5ilhk2bgfyvgsvmj/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openpmd-api-0.11.1-fhdp7nfpzfaaz52o5ilhk2bgfyvgsvmj/lib64;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/adios2-2.8.2-bkhq7gjkpxi7xs53fcbhd4fgpxgiv33h/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/bzip2-1.0.8-ya4ug5vmw7aniehgduokbk7vjk6nnpiu/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/c-blosc-1.21.1-ilmlanom4taf3dzebghkme2pphyqw4ni/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/lz4-1.9.3-exgubctolejmf5x45kogxvp55ax4vxmi/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/snappy-1.1.9-iwbmapmpzvxgeqk6gw5mdgszukctik5u/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7sovaylq/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zstd-1.5.2-eejca7y2axvxog65dssarq4ebcj2otlu/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libfabric-1.14.1-o2jqamajbpuia77ukdic2gl4uecomxpd/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libffi-3.4.2-mhxy22owln7ofc6s3auicpwmcdvcydar/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libpng-1.6.37-kf3i42l7yqde2a43egkmnqkwrnrr7dhd/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-2.7.1-i5ayu7korr7gkh6qtnglfrh7uii2a2eo/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libpciaccess-0.16-fdqihaqivzq7jfv2bvhl4jtpji6lhi5n/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libxml2-2.9.13-5crpofret7ivv3tp5ls6zv6msqot2xnx/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libiconv-1.16-yuly674bkth5o6pwr2r4yjlqn37veokj/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/xz-5.2.5-453s3chw5hjari5ttv4t26jj3vqogyjr/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/ncurses-6.2-vwwyeulbfzoa4b3eimalm52bwtcf77rf/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/numactl-2.0.14-wf2qo4fov2buxvoj4xbgyj7g27lbaq6q/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/pmix-4.1.2-77l2xoffatjou7q7asvgoe5x4wkkcx45/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libevent-2.1.12-eikbakv4aqqnd2i5a7rminoccl2rw6a6/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openssl-1.1.1q-3s72rwr6sei7t2bgnalx6sqno7xs6xqb/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/sz-2.1.12.2-fpizk225dbj7ifhfnpjyma6nrtoltxrr/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zfp-0.5.5-k3vqem5tldcx4bdejxrvqe6hgrhdb3nk/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hdf5-1.12.2-godyvkcwlaxwahxwhmsquzba4l5vd6lx/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/mpark-variant-1.4.0-mp65jzqsihdu4rjc2qzeksxhje2ujbp2/lib;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/nlohmann-json-3.10.5-gbep6sj7r6o77skebrmynsdcs35kjx52/lib' '-DCMAKE_PREFIX_PATH:STRING=/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/nlohmann-json-3.10.5-gbep6sj7r6o77skebrmynsdcs35kjx52;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/mpark-variant-1.4.0-mp65jzqsihdu4rjc2qzeksxhje2ujbp2;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hdf5-1.12.2-godyvkcwlaxwahxwhmsquzba4l5vd6lx;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/adios2-2.8.2-bkhq7gjkpxi7xs53fcbhd4fgpxgiv33h;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zfp-0.5.5-k3vqem5tldcx4bdejxrvqe6hgrhdb3nk;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/sz-2.1.12.2-fpizk225dbj7ifhfnpjyma6nrtoltxrr;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/pmix-4.1.2-77l2xoffatjou7q7asvgoe5x4wkkcx45;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libevent-2.1.12-eikbakv4aqqnd2i5a7rminoccl2rw6a6;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/numactl-2.0.14-wf2qo4fov2buxvoj4xbgyj7g27lbaq6q;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-2.7.1-i5ayu7korr7gkh6qtnglfrh7uii2a2eo;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libxml2-2.9.13-5crpofret7ivv3tp5ls6zv6msqot2xnx;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/xz-5.2.5-453s3chw5hjari5ttv4t26jj3vqogyjr;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libpciaccess-0.16-fdqihaqivzq7jfv2bvhl4jtpji6lhi5n;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libpng-1.6.37-kf3i42l7yqde2a43egkmnqkwrnrr7dhd;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libffi-3.4.2-mhxy22owln7ofc6s3auicpwmcdvcydar;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libfabric-1.14.1-o2jqamajbpuia77ukdic2gl4uecomxpd;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/c-blosc-1.21.1-ilmlanom4taf3dzebghkme2pphyqw4ni;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zstd-1.5.2-eejca7y2axvxog65dssarq4ebcj2otlu;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/snappy-1.1.9-iwbmapmpzvxgeqk6gw5mdgszukctik5u;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/lz4-1.9.3-exgubctolejmf5x45kogxvp55ax4vxmi;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openssl-1.1.1q-3s72rwr6sei7t2bgnalx6sqno7xs6xqb;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7sovaylq;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/ncurses-6.2-vwwyeulbfzoa4b3eimalm52bwtcf77rf;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/bzip2-1.0.8-ya4ug5vmw7aniehgduokbk7vjk6nnpiu;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/libiconv-1.16-yuly674bkth5o6pwr2r4yjlqn37veokj' '-DBUILD_SHARED_LIBS:BOOL=ON' '-DopenPMD_USE_MPI:BOOL=ON' '-DopenPMD_USE_HDF5:BOOL=ON' '-DopenPMD_USE_ADIOS1:BOOL=OFF' '-DopenPMD_USE_ADIOS2:BOOL=ON' '-DopenPMD_USE_PYTHON:BOOL=OFF' '-DBUILD_TESTING:BOOL=OFF' '-DBUILD_EXAMPLES:BOOL=OFF' '-DopenPMD_USE_INTERNAL_JSON:BOOL=OFF' '-DopenPMD_USE_INTERNAL_VARIANT:BOOL=OFF' '/tmp/root/spack-stage/spack-stage-openpmd-api-0.11.1-fhdp7nfpzfaaz52o5ilhk2bgfyvgsvmj/spack-src'

1 error found in build log:
     15    -- Found MPI_C: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmi
           py3bjhsk5dbioidlwxm2oeyqso4b/lib/libmpi.so (found version "3.1")
     16    -- Found MPI_CXX: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cq
           mipy3bjhsk5dbioidlwxm2oeyqso4b/lib/libmpi.so (found version "3.1")
     17    -- Found MPI: TRUE (found version "3.1")
     18    -- Found nlohmann_json: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/nlohmann-j
           son-3.10.5-gbep6sj7r6o77skebrmynsdcs35kjx52/lib/cmake/nlohmann_json/nlohmann_jsonConfig.
           cmake (found suitable version "3.10.5", minimum required is "3.7.0")
     19    -- nlohmann-json: Found version 3.10.5
     20    -- Found HDF5: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hdf5-1.12.2-godyvkc
           wlaxwahxwhmsquzba4l5vd6lx/lib/libhdf5.so;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-
           11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/lib/libmpi.so (found suitable vers
           ion "1.12.2", minimum required is "1.8.13") found components: C
  >> 21    CMake Error at CMakeLists.txt:157 (message):
     22      Found MPI but only serial version of HDF5.  Either set openPMD_USE_MPI=OFF
     23      to disable MPI or set openPMD_USE_HDF5=OFF to disable HDF5 or provide a
     24      parallel install of HDF5.
     25    
     26    
     27    -- Configuring incomplete, errors occurred!

See build log for details:
  /tmp/root/spack-stage/spack-stage-openpmd-api-0.11.1-fhdp7nfpzfaaz52o5ilhk2bgfyvgsvmj/spack-build-out.txt

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/spliced/experiment/spack.py", line 121, in do_install
    spec.package.do_install(force=True)
  File "/spack/lib/spack/spack/package_base.py", line 1905, in do_install
    builder.install()
  File "/spack/lib/spack/spack/installer.py", line 1699, in install
    self._install_task(task)
  File "/spack/lib/spack/spack/installer.py", line 1233, in _install_task
    spack.build_environment.start_build_process(
  File "/spack/lib/spack/spack/build_environment.py", line 1200, in start_build_process
    raise child_result
spack.build_environment.ChildError: ProcessError: Command exited with status 1:
    'cmake' '-G' 'Unix Makefiles' '-DCMAKE_INSTALL_PREFIX:STRING=/spack/opt/spack/linux-ubuntu22.04-
```

### slate: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package slate@2020.10.00 --splice cmake --runner spack --replace cmake --experiment slate --outfile /results/slate/2020.10.00/cmake/experiment.json

1 error found in build log:
     16       flags:
     17       -DFORTRAN_ADD_                                   no (didn't link: routine not found)
     18       -DFORTRAN_LOWER                                  no (didn't link: routine not found)
     19       -DFORTRAN_UPPER                                  no (didn't link: routine not found)
     20    
     21       BLAS library not found.
  >> 22    CMake Error at CMakeLists.txt:295 (message):
     23      BLAS++ requires a BLAS library and none was found.  Ensure that it is
     24      accessible in environment variables $CPATH, $LIBRARY_PATH, and
     25      $LD_LIBRARY_PATH.
     26    
     27    
     28    -- Configuring incomplete, errors occurred!

See build log for details:
  /tmp/root/spack-stage/spack-stage-blaspp-2020.10.02-ybvedwhzmwgydorzzpqz2yjfpetykn34/spack-build-out.txt
```

### petsc: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package petsc@3.10.0 --splice python --runner spack --replace python --experiment petsc --outfile /results/petsc/3.10.0/python/experiment.json


==> [2022-07-28-19:11:54.887419, 11] 11: superlu-dist: Executing phase: 'cmake'
==> [2022-07-28-19:11:56.389064, 11] 11: superlu-dist: Executing phase: 'build'
==> [2022-07-28-19:12:07.225604, 11] WRITE LOCK (spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73): /tmp/root/spack-stage/.lock[1936176548018551543:1] [Released at 19:12:07.225561] 
==> [2022-07-28-19:12:07.248230, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8'

33 errors found in build log:
     936     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive1_ABglobal.dir/link.txt --verbose=1
     937     [ 82%] Building C object EXAMPLE/CMakeFiles/pddrive2.dir/dcreate_matrix.c.o
     938     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/sp
             ack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC 
             -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg
             5x4iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/meti
             s-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-s
             uperlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/includ
             e -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnj
             kg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT EXAMPL
             E/CMakeFiles/pddrive2.dir/dcreate_matrix.c.o -MF CMakeFiles/pddrive2.dir/dcreate_matri
             x.c.o.d -o CMakeFiles/pddrive2.dir/dcreate_matrix.c.o -c /tmp/root/spack-stage/spack-s
             tage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/EXAMPLE/dcreate_mat
             rix.c
     939     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive1_ABglobal.dir/pddrive1_AB
             global.c.o -o pddrive1_ABglobal  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-
             dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/spack/opt/spack/l
             inux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/l
             ib ../SRC/libsuperlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2
             .0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/op
             t/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi
             6xynrp/lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.
             1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     940     [ 82%] Building C object TEST/CMakeFiles/pdtest.dir/dcreate_matrix.c.o
     941     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/TEST && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
             penmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC -I/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4
             iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5
             .1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/linux
             -ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -
             I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5
             x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT TEST/CMak
             eFiles/pdtest.dir/dcreate_matrix.c.o -MF CMakeFiles/pdtest.dir/dcreate_matrix.c.o.d -o
              CMakeFiles/pdtest.dir/dcreate_matrix.c.o -c /tmp/root/spack-stage/spack-stage-superlu
             -dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/TEST/dcreate_matrix.c
  >> 942     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 943     collect2: error: ld returned 1 exit status
  >> 944     make[2]: *** [EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/build.make:102: EXAMPLE/pddrive_
             ABglobal] Error 1
     945     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 946     make[1]: *** [CMakeFiles/Makefile2:385: EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/all] E
             rror 2
     947     make[1]: *** Waiting for unfinished jobs....
     948     [ 83%] Building C object TEST/CMakeFiles/pdtest.dir/pdcompute_resid.c.o
     949     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/TEST && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
             penmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC -I/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4
             iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5
             .1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/linux
             -ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -
             I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5
             x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT TEST/CMak
             eFiles/pdtest.dir/pdcompute_resid.c.o -MF CMakeFiles/pdtest.dir/pdcompute_resid.c.o.d 
             -o CMakeFiles/pdtest.dir/pdcompute_resid.c.o -c /tmp/root/spack-stage/spack-stage-supe
             rlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/TEST/pdcompute_resid.c
     950     [ 84%] Linking C executable pddrive4
  >> 951     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
     952     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive4.dir/link.txt --verbose=1
  >> 953     collect2: error: ld returned 1 exit status
  >> 954     make[2]: *** [EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/build.make:102: EXAMPLE/pddrive
             1_ABglobal] Error 1
     955     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 956     make[1]: *** [CMakeFiles/Makefile2:411: EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/all] 
             Error 2
     957     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive4.dir/pddrive4.c.o CMakeFi
             les/pddrive4.dir/dcreate_matrix.c.o -o pddrive4  -Wl,-rpath,/tmp/root/spack-stage/spac
             k-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/s
             pack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuq
             vsax4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so
              -lm -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3
             lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc
             -11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     958     [ 84%] Building C object EXAMPLE/CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o
     959     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/sp
             ack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC 
             -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg
             5x4iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/meti
             s-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-s
             uperlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/includ
             e -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnj
             kg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT EXAMPL
             E/CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o -MF CMakeFiles/pddrive2.dir/dcr
             eate_matrix_perturbed.c.o.d -o CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o -c
              /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73
             /spack-src/EXAMPLE/dcreate_matrix_perturbed.c
     960     [ 85%] Linking C executable pddrive
     961     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive.dir/link.txt --verbose=1
     962     [ 85%] Linking C executable pddrive1

     ...

     966     [ 86%] Linking C executable pddrive3
     967     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive3.dir/link.txt --verbose=1
     968     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive3.dir/pddrive3.c.o CMakeFi
             les/pddrive3.dir/dcreate_matrix.c.o -o pddrive3  -Wl,-rpath,/tmp/root/spack-stage/spac
             k-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/s
             pack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuq
             vsax4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so
              -lm -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3
             lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc
             -11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     969     [ 86%] Linking C executable pdtest
     970     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/TEST && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/c
             make-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
             /pdtest.dir/link.txt --verbose=1
     971     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pdtest.dir/pdtest.c.o CMakeFiles/
             pdtest.dir/dcreate_matrix.c.o CMakeFiles/pdtest.dir/pdcompute_resid.c.o -o pdtest  -Wl
             ,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjj
             w3wdb73/spack-build-atky62e/SRC:/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
             openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.5.4.0 /
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihu
             qvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubuntu22.04-skylake/gc
             c-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg
             /lib -lmetis
  >> 972     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 973     collect2: error: ld returned 1 exit status
  >> 974     make[2]: *** [EXAMPLE/CMakeFiles/pddrive4.dir/build.make:118: EXAMPLE/pddrive4] Error 
             1
     975     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 976     make[1]: *** [CMakeFiles/Makefile2:359: EXAMPLE/CMakeFiles/pddrive4.dir/all] Error 2
  >> 977     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 978     collect2: error: ld returned 1 exit status
  >> 979     make[2]: *** [EXAMPLE/CMakeFiles/pddrive.dir/build.make:118: EXAMPLE/pddrive] Error 1
     980     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 981     make[1]: *** [CMakeFiles/Makefile2:255: EXAMPLE/CMakeFiles/pddrive.dir/all] Error 2
  >> 982     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 983     collect2: error: ld returned 1 exit status
  >> 984     make[2]: *** [EXAMPLE/CMakeFiles/pddrive1.dir/build.make:118: EXAMPLE/pddrive1] Error 
             1
     985     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 986     make[1]: *** [CMakeFiles/Makefile2:281: EXAMPLE/CMakeFiles/pddrive1.dir/all] Error 2
  >> 987     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 988     collect2: error: ld returned 1 exit status
  >> 989     make[2]: *** [EXAMPLE/CMakeFiles/pddrive3.dir/build.make:118: EXAMPLE/pddrive3] Error 
             1
     990     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 991     make[1]: *** [CMakeFiles/Makefile2:333: EXAMPLE/CMakeFiles/pddrive3.dir/all] Error 2
     992     [ 87%] Linking C executable pddrive2
     993     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive2.dir/link.txt --verbose=1
     994     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive2.dir/pddrive2.c.o CMakeFi
             les/pddrive2.dir/dcreate_matrix.c.o CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c
             .o -o pddrive2  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62
             eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsupe
             rlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.2
             0-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubu
             ntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparm
             etis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfq
             wrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 995     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 996     collect2: error: ld returned 1 exit status
  >> 997     make[2]: *** [TEST/CMakeFiles/pdtest.dir/build.make:134: TEST/pdtest] Error 1
     998     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 999     make[1]: *** [CMakeFiles/Makefile2:229: TEST/CMakeFiles/pdtest.dir/all] Error 2
  >> 1000    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 1001    collect2: error: ld returned 1 exit status
  >> 1002    make[2]: *** [EXAMPLE/CMakeFiles/pddrive2.dir/build.make:134: EXAMPLE/pddrive2] Error 
             1
     1003    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 1004    make[1]: *** [CMakeFiles/Makefile2:307: EXAMPLE/CMakeFiles/pddrive2.dir/all] Error 2
     1005    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 1006    make: *** [Makefile:149: all] Error 2

See build log for details:
  /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-out.txt
```


### tau: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package tau@2.23.1 --splice hwloc --runner spack --replace hwloc --experiment tau --outfile /results/tau/2.23.1/hwloc/experiment.json

==> [2022-07-28-19:13:27.872193, 11] 11: tau: Executing phase: 'install'
==> [2022-07-28-19:13:39.528399, 11] WRITE LOCK (spack-stage-tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375): /tmp/root/spack-stage/.lock[6592751899076257295:1] [Released at 19:13:39.528360] 
==> [2022-07-28-19:13:39.549241, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8' 'install'

15 errors found in build log:
     57      TAU: PDT: Using binary rewriting capabilities from PEBIL in tau_pebil_rewrite
     58      ====================================================
     59       Copy /tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/sp
             ack-src/tools/src/contrib/CubeReader.jar to /spack/opt/spack/linux-ubuntu22.04-skylake
             /gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/x86_64/lib
     60      ====================================================
     61      ... done
     62      ***********************************************************************
  >> 63      grep: ./utils/FixMakefile.info: No such file or directory
  >> 64      grep: ./utils/FixMakefile.sed: No such file or directory
     65      NOTE: Enabled Profiling. Compiling with -DPROFILING_ON
     66      NOTE: Building POSIX I/O wrapper
     67      NOTE: GNU gfortran compiler specific options used
     68      NOTE: Using PAPI interface for Hardware Performance Counters ***
     69      NOTE: Using PAPI with -lpfm option ***
     70      NOTE: Using default cc compiler.

     ...

     160     rm -f trace2profile/trace2profile  handlers.o handlers.*.~* readTrace.o readTrace.*.~*
              Makefile.~* *.o otf2profile
     161     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/utils/otf2profile'
     162     make[1]: Entering directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/spack-src/examples/instrument'
     163     /bin/rm -f simple.o simple
     164     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/examples/instrument'
     165     make[1]: Entering directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/spack-src/examples/threads'
  >> 166     Makefile:16: /tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctou
             w375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt: No such file or directory
  >> 167     make[1]: *** No rule to make target '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spff
             masbg5g7lkhhi3q3vcjtctouw375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt'.  Sto
             p.
     168     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/examples/threads'
     169     make[1]: Entering directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/spack-src/examples/cthreads'
  >> 170     Makefile:16: /tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctou
             w375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt: No such file or directory
  >> 171     make[1]: *** No rule to make target '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spff
             masbg5g7lkhhi3q3vcjtctouw375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt'.  Sto
             p.
     172     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/examples/cthreads'
     173     make[1]: Entering directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/spack-src/examples/fortran'
     174     /bin/rm -f hello.o hello
     175     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/examples/fortran'
     176     make[1]: Entering directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/spack-src/examples/f90'
     177     /bin/rm -f cubes.o cubes
     178     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/examples/f90'
     179     make[1]: Entering directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/spack-src/examples/autoinstrument'
  >> 180     Makefile:16: /tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctou
             w375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt: No such file or directory
  >> 181     make[1]: *** No rule to make target '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spff
             masbg5g7lkhhi3q3vcjtctouw375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt'.  Sto
             p.
     182     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/examples/autoinstrument'
     183     make[1]: Entering directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/spack-src/examples/reduce'
  >> 184     Makefile:16: /tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctou
             w375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt: No such file or directory
  >> 185     make[1]: *** No rule to make target '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spff
             masbg5g7lkhhi3q3vcjtctouw375/spack-src/x86_64/lib/Makefile.tau-papi-pthread-pdt'.  Sto
             p.
     186     make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/examples/reduce'
     187     touch .clean
     188     Determining Configuration...
     189     System previously configured as a x86_64
     190     *********** RECURSIVELY MAKING SUBDIRECTORIES ***********
     191     *** COMPILING src/TraceInput DIRECTORY

     ...

     231     g++    -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.2
             3.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04
             -skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spac
             k/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnv
             nvh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-m
             aster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.
             04-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,
             /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3ba
             exsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.
             0.0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.
             04-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spac
             k/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7
             sovaylq/lib -I../include  -w         -DTAU_USE_SIZE_INSTEAD_OF_SIZEOF  -I/spack/opt/sp
             ack/linux-ubuntu22.04-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/i
             nclude -c tau_instrument.cpp
     232     g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib -c -o process_c.o process_c.cc
     233     g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23.1-spffmasb
             g5g7lkhhi3q3vcjtctouw375/include -I. -c readTrace.cpp
     234     g++    -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.2
             3.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04
             -skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spac
             k/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnv
             nvh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-m
             aster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.
             04-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,
             /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3ba
             exsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.
             0.0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.
             04-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spac
             k/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7
             sovaylq/lib -I../include  -w         -DTAU_USE_SIZE_INSTEAD_OF_SIZEOF  -I/spack/opt/sp
             ack/linux-ubuntu22.04-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/i
             nclude -c tau_selective.cpp
     235     g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib -I../include  -w       -DTAU_GNU -DTAU_DOT_H_LESS_HEADERS -fPIC     tau2otf
             2.cpp -c -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hg
             bte4u37n3baexsaswuox/include
     236     tau_instrumentor.cpp: In function 'int printTauAllocStmt(std::ifstream&, std::ofstream
             &, char*, std::vector<itemRef*>::iterator&, char*&)':
  >> 237     tau_instrumentor.cpp:2702:47: error: no match for 'operator==' (operand types are 'std
             ::basic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} and 'long int'
             )
     238      2702 |       if (istr.getline(allocstmt, INBUF_SIZE) == NULL) {
     239           |                                               ^
     240     tau_instrumentor.cpp:2702:47: note: candidate: 'operator==(int, long int)' (built-in)
     241     tau_instrumentor.cpp:2702:47: note:   no known conversion for argument 1 from 'std::ba
             sic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} to 'int'
     242     In file included from /usr/include/c++/11/iosfwd:40,
     243                      from /usr/include/c++/11/ios:38,

     ...

     894       408 |   operator==(const error_condition& __lhs, const error_code& __rhs) noexcept
     895           |   ^~~~~~~~
     896     /usr/include/c++/11/system_error:408:37: note:   no known conversion for argument 1 fr
             om 'std::basic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} to 'con
             st std::error_condition&'
     897       408 |   operator==(const error_condition& __lhs, const error_code& __rhs) noexcept
     898           |              ~~~~~~~~~~~~~~~~~~~~~~~^~~~~
     899     tau_instrumentor.cpp: In function 'int printTauDeallocStmt(std::ifstream&, std::ofstre
             am&, char*, std::vector<itemRef*>::iterator&, bool, char*&)':
  >> 900     tau_instrumentor.cpp:2810:50: error: no match for 'operator==' (operand types are 'std
             ::basic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} and 'long int'
             )
     901      2810 |        if (istr.getline(deallocstmt, INBUF_SIZE) == NULL)
     902           |                                                  ^
     903     tau_instrumentor.cpp:2810:50: note: candidate: 'operator==(int, long int)' (built-in)
     904     tau_instrumentor.cpp:2810:50: note:   no known conversion for argument 1 from 'std::ba
             sic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} to 'int'
     905     In file included from /usr/include/c++/11/iosfwd:40,
     906                      from /usr/include/c++/11/ios:38,

     ...

     1558      408 |   operator==(const error_condition& __lhs, const error_code& __rhs) noexcept
     1559          |   ^~~~~~~~
     1560    /usr/include/c++/11/system_error:408:37: note:   no known conversion for argument 1 fr
             om 'std::basic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} to 'con
             st std::error_condition&'
     1561      408 |   operator==(const error_condition& __lhs, const error_code& __rhs) noexcept
     1562          |              ~~~~~~~~~~~~~~~~~~~~~~~^~~~~
     1563    tau_instrumentor.cpp: In function 'int printTauIOStmt(std::ifstream&, std::ofstream&, 
             char*, std::vector<itemRef*>::iterator&, bool, char*&)':
  >> 1564    tau_instrumentor.cpp:2923:42: error: no match for 'operator==' (operand types are 'std
             ::basic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} and 'long int'
             )
     1565     2923 |     if (istr.getline(iostmt, INBUF_SIZE) == NULL)
     1566          |                                          ^
     1567    tau_instrumentor.cpp:2923:42: note: candidate: 'operator==(int, long int)' (built-in)
     1568    tau_instrumentor.cpp:2923:42: note:   no known conversion for argument 1 from 'std::ba
             sic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} to 'int'
     1569    In file included from /usr/include/c++/11/iosfwd:40,
     1570                     from /usr/include/c++/11/ios:38,

     ...

     2221      408 |   operator==(const error_condition& __lhs, const error_code& __rhs) noexcept
     2222          |   ^~~~~~~~
     2223    /usr/include/c++/11/system_error:408:37: note:   no known conversion for argument 1 fr
             om 'std::basic_istream<char>::__istream_type' {aka 'std::basic_istream<char>'} to 'con
             st std::error_condition&'
     2224      408 |   operator==(const error_condition& __lhs, const error_code& __rhs) noexcept
     2225          |              ~~~~~~~~~~~~~~~~~~~~~~~^~~~~
     2226    g++    -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.2
             3.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04
             -skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spac
             k/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnv
             nvh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-m
             aster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.
             04-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,
             /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3ba
             exsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.
             0.0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.
             04-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spac
             k/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7
             sovaylq/lib -I../include  -w         -DTAU_USE_SIZE_INSTEAD_OF_SIZEOF  -I/spack/opt/sp
             ack/linux-ubuntu22.04-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/i
             nclude -c tau_wrap.cpp
  >> 2227    make[1]: *** [Makefile:88: tau_instrumentor.o] Error 1
     2228    make[1]: *** Waiting for unfinished jobs....
     2229    g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib -c -o process_f.o process_f.cc
     2230    g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib -c -o process_omp.o process_omp.cc
     2231    trace2profile.cpp: In function 'void PrintSnapshot(double, Thread&, bool)':
     2232    trace2profile.cpp:535:23: warning: ignoring return value of 'int system(const char*)' 
             declared with attribute 'warn_unused_result' [-Wunused-result]
     2233      535 |                 system(cmd.c_str());

     ...

     2242    g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib -c -o handler.o handler.cc
     2243    g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23.1-spffmasb
             g5g7lkhhi3q3vcjtctouw375/include -I. -o trace2profile handlers.o readTrace.o trace2pro
             file.o -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7
             lkhhi3q3vcjtctouw375/x86_64/lib -lTAU_traceinput-papi-pthread-pdt
     2244    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/utils/trace2profile'
     2245    g++   -O2 -g -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tau-2.23
             .1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/tau-2.23.1-spffmasbg5g7lkhhi3q3vcjtctouw375/lib64 -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/binutils-2.38-zqz47r4l4a4kwm2aihemxnvn
             vh5cf7e2/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-ma
             ster-c5kous2suaihqskeyz7pgsoo5o6gfzu4/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/libunwind-1.6.2-yxd45ely5u4e7hzoytnywutyhqmn2byg/lib -Wl,-rpath,/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/otf2-2.3-vsxsupi473hgbte4u37n3bae
             xsaswuox/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/papi-6.0
             .0.1-y3lgty22prsm6afapbvqpoblackbsxbg/lib -Wl,-rpath,/spack/opt/spack/linux-ubuntu22.0
             4-skylake/gcc-11.2.0/pdt-3.25.1-2wuoorprwqorusgcf4nrb7zlpmczo2rz/lib -Wl,-rpath,/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/zlib-1.2.12-y3vm6i6g7ot663ojvxtookqc7s
             ovaylq/lib opari.o process_c.o process_f.o process_omp.o ompragma.o ompragma_c.o ompra
             gma_f.o ompregion.o handler.o  -o opari
     2246    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/utils/opari'
     2247    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-tau-2.23.1-spffmasbg5g7l
             khhi3q3vcjtctouw375/spack-src/utils'
  >> 2248    make: *** [Makefile:167: install] Error 2
```

### qthreads: SUCCESS

...but there are missing symbols (looks like lib C with @@) so we don't run smeagle.

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package qthreads@1.10 --splice hwloc@master --runner spack --replace hwloc --experiment qthreads --outfile /results/qthreads/1.10/hwloc/experiment.json
```

most splices fail, e.g.,

```bash
==> hwloc: Executing phase: 'autoreconf'
==> hwloc: Executing phase: 'configure'
==> hwloc: Executing phase: 'build'
==> hwloc: Executing phase: 'install'
==> hwloc: Successfully installed hwloc-2.0.1-g3ka6m442ilr6fvpkazjizhphjd55e35
  Fetch: 1.24s.  Build: 15.11s.  Total: 16.35s.
[+] /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hwloc-2.0.1-g3ka6m442ilr6fvpkazjizhphjd55e35
Traceback (most recent call last):
  File "/spack/lib/spack/spack/spec.py", line 3961, in __getitem__
    value = next(
StopIteration

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/spliced/experiment/spack.py", line 236, in do_splice
    spack.rewiring.rewire(spliced_spec)
  File "/spack/lib/spack/spack/rewiring.py", line 49, in rewire
    rewire_node(spec, explicit)
  File "/spack/lib/spack/spack/rewiring.py", line 83, in rewire_node
    spliced_build_dep_prefix = get_container_prefix(spec, spec[build_dep.name].prefix)
  File "/spack/lib/spack/spack/spec.py", line 3970, in __getitem__
    raise KeyError("No spec with name %s in %s" % (name, self))
KeyError: 'No spec with name autoconf in qthreads@1.10%gcc@11.2.0+hwloc~spawn_cache+static patches=d9c7ac0,f708d93 scheduler=nemesis stack_size=4096 arch=linux-ubuntu22.04-skylake ^diffutils@3.8%gcc@11.2.0 arch=linux-ubuntu22.04-skylake ^hwloc@2.1.0%gcc@11.2.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm+shared arch=linux-ubuntu22.04-skylake ^libiconv@1.16%gcc@11.2.0 libs=shared,static arch=linux-ubuntu22.04-skylake ^libpciaccess@0.16%gcc@11.2.0 arch=linux-ubuntu22.04-skylake ^libsigsegv@2.13%gcc@11.2.0 arch=linux-ubuntu22.04-skylake ^libtool@2.4.7%gcc@11.2.0 arch=linux-ubuntu22.04-skylake ^libxml2@2.9.13%gcc@11.2.0~python arch=linux-ubuntu22.04-skylake ^m4@1.4.19%gcc@11.2.0+sigsegv patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-skylake ^ncurses@6.2%gcc@11.2.0~symlinks~termlib abi=none arch=linux-ubuntu22.04-skylake ^pkgconf@1.8.0%gcc@11.2.0 arch=linux-ubuntu22.04-skylake ^util-macros@1.19.3%gcc@11.2.0 arch=linux-ubuntu22.04-skylake ^xz@5.2.5%gcc@11.2.0~pic libs=shared,static arch=linux-ubuntu22.04-skylake ^zlib@1.2.12%gcc@11.2.0+optimize+pic+shared patches=0d38234 arch=linux-ubuntu22.04-skylake'
```

hwloc@master works, but missing symbols from the getgo. Libabigail/abi lab cannot predict because
we only have exact matching dependency libraries. Also:

```bash
Cannot find needed library libhwloc.so.5
```

For "missing" symbols:

> We'd take stderr@GLIBC_2.2.5, look up 'stderr' in .symver, follow the link to the PLT and then version check the GLIBC_2.2.5 suffix. There are details missing there, but that would be the gist.


### superlu-dist: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package superlu-dist@5.0.0 --splice cmake@3.23.1 --runner spack --replace cmake --experiment superlu-dist --outfile /results/superlu-dist/5.0.0/cmake/experiment.json

  >> 791    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so
            : undefined reference to `_gfortran_concat_string'

And re-run with another cmake splice

==> [2022-07-28-19:17:22.487917, 11] WRITE LOCK (spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k): /tmp/root/spack-stage/.lock[6505392650183886231:1] [Released at 19:17:22.487857] 
==> [2022-07-28-19:17:22.507084, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8'

33 errors found in build log:
     541    [ 73%] Linking C executable pddrive1_ABglobal
     542    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive1_ABglobal.dir/link.txt --verbose=1
     543    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive1_ABglobal.dir/pddrive1_ABglobal.c.o -o pd
            drive1_ABglobal  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/linux-ubuntu22.04-s
            kylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperl
            u_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4
            urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubuntu2
            2.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis 
            -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
            7lbb7q7gz77sg/lib -lmetis
     544    [ 74%] Linking C executable pddrive2_ABglobal
     545    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive2_ABglobal.dir/link.txt --verbose=1
     546    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive2_ABglobal.dir/pddrive2_ABglobal.c.o -o pd
            drive2_ABglobal  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/linux-ubuntu22.04-s
            kylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperl
            u_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4
            urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubuntu2
            2.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis 
            -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
            7lbb7q7gz77sg/lib -lmetis
  >> 547    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 548    collect2: error: ld returned 1 exit status
  >> 549    make[2]: *** [EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/build.make:102: EXAMPLE/pddrive_A
            Bglobal] Error 1
     550    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 551    make[1]: *** [CMakeFiles/Makefile2:313: EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/all] Er
            ror 2
     552    make[1]: *** Waiting for unfinished jobs....
  >> 553    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 554    collect2: error: ld returned 1 exit status
  >> 555    make[2]: *** [EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/build.make:102: EXAMPLE/pddrive1
            _ABglobal] Error 1
     556    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 557    make[1]: *** [CMakeFiles/Makefile2:339: EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/all] E
            rror 2
     558    [ 75%] Linking C executable pddrive
     559    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive.dir/link.txt --verbose=1
     560    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive.dir/pddrive.c.o CMakeFiles/pddrive.dir/dc
            reate_matrix.c.o -o pddrive  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-
            5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/linux-u
            buntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../S
            RC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openb
            las-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/l
            inux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib
             -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxak
            ba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 561    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
     562    [ 76%] Linking C executable pddrive4
     563    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive4.dir/link.txt --verbose=1
  >> 564    collect2: error: ld returned 1 exit status
     565    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive4.dir/pddrive4.c.o CMakeFiles/pddrive4.dir
            /dcreate_matrix.c.o -o pddrive4  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 566    make[2]: *** [EXAMPLE/CMakeFiles/pddrive2_ABglobal.dir/build.make:102: EXAMPLE/pddrive2
            _ABglobal] Error 1
     567    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 568    make[1]: *** [CMakeFiles/Makefile2:365: EXAMPLE/CMakeFiles/pddrive2_ABglobal.dir/all] E
            rror 2
     569    [ 77%] Linking C executable pddrive1
     570    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive1.dir/link.txt --verbose=1
     571    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive1.dir/pddrive1.c.o CMakeFiles/pddrive1.dir
            /dcreate_matrix.c.o -o pddrive1  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     572    [ 78%] Linking C executable pddrive3
     573    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive3.dir/link.txt --verbose=1
     574    [ 79%] Linking C executable pddrive2
     575    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive2.dir/link.txt --verbose=1
     576    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive3.dir/pddrive3.c.o CMakeFiles/pddrive3.dir
            /dcreate_matrix.c.o -o pddrive3  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     577    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive2.dir/pddrive2.c.o CMakeFiles/pddrive2.dir
            /dcreate_matrix.c.o -o pddrive2  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 578    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 579    collect2: error: ld returned 1 exit status
  >> 580    make[2]: *** [EXAMPLE/CMakeFiles/pddrive.dir/build.make:118: EXAMPLE/pddrive] Error 1
     581    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 582    make[1]: *** [CMakeFiles/Makefile2:183: EXAMPLE/CMakeFiles/pddrive.dir/all] Error 2
  >> 583    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 584    collect2: error: ld returned 1 exit status
  >> 585    make[2]: *** [EXAMPLE/CMakeFiles/pddrive1.dir/build.make:118: EXAMPLE/pddrive1] Error 1
     586    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 587    make[1]: *** [CMakeFiles/Makefile2:209: EXAMPLE/CMakeFiles/pddrive1.dir/all] Error 2
  >> 588    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 589    collect2: error: ld returned 1 exit status
  >> 590    make[2]: *** [EXAMPLE/CMakeFiles/pddrive4.dir/build.make:118: EXAMPLE/pddrive4] Error 1
     591    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 592    make[1]: *** [CMakeFiles/Makefile2:287: EXAMPLE/CMakeFiles/pddrive4.dir/all] Error 2
  >> 593    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 594    collect2: error: ld returned 1 exit status
  >> 595    make[2]: *** [EXAMPLE/CMakeFiles/pddrive2.dir/build.make:118: EXAMPLE/pddrive2] Error 1
     596    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 597    make[1]: *** [CMakeFiles/Makefile2:235: EXAMPLE/CMakeFiles/pddrive2.dir/all] Error 2
  >> 598    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 599    collect2: error: ld returned 1 exit status
  >> 600    make[2]: *** [EXAMPLE/CMakeFiles/pddrive3.dir/build.make:118: EXAMPLE/pddrive3] Error 1
     601    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 602    make[1]: *** [CMakeFiles/Makefile2:261: EXAMPLE/CMakeFiles/pddrive3.dir/all] Error 2
     603    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 604    make: *** [Makefile:149: all] Error 2
```

### fortilinos: UNKNOWN

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package fortrilinos@2.0.0 --splice trilinos --runner spack --replace trilinos --experiment fortrilinos --outfile /results/fortrilinos/2.0.0/trilinos/experiment.json
```

This is too chonky to build on my laptop.

### omega-h: UNKNOWN

requires trillinos too, lol

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package omega-h@9.13.13 --splice openmpi --runner spack --replace openmpi --experiment omega-h --outfile /results/omega-h/9.13.13/openmpi/experiment.json
```

### hdf5: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package hdf5@1.10.0 --splice pkgconf --runner spack --replace pkgconf --experiment hdf5 --outfile /results/hdf5/1.10.0/pkgconf/experiment.json
```

However, looks like elfcall can't find:

```bash
Cannot find needed library libmpi.so.40
```
And the main (master) branch can't be relocated because it's a longer path.

### openpmd-api: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package openpmd-api@0.11.1 --splice openmpi@master --runner spack --replace openmpi --experiment openpmd-api --outfile /results/openpmd-api/0.11.1/openmpi/experiment.json


1:BOOL=OFF' '-DopenPMD_USE_ADIOS2:BOOL=ON' '-DopenPMD_USE_PYTHON:BOOL=OFF' '-DBUILD_TESTING:BOOL=OFF' '-DBUILD_EXAMPLES:BOOL=OFF' '-DopenPMD_USE_INTERNAL_JSON:BOOL=OFF' '-DopenPMD_USE_INTERNAL_VARIANT:BOOL=OFF' '/tmp/root/spack-stage/spack-stage-openpmd-api-0.11.1-fhdp7nfpzfaaz52o5ilhk2bgfyvgsvmj/spack-src'

1 error found in build log:
     15    -- Found MPI_C: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmi
           py3bjhsk5dbioidlwxm2oeyqso4b/lib/libmpi.so (found version "3.1")
     16    -- Found MPI_CXX: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cq
           mipy3bjhsk5dbioidlwxm2oeyqso4b/lib/libmpi.so (found version "3.1")
     17    -- Found MPI: TRUE (found version "3.1")
     18    -- Found nlohmann_json: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/nlohmann-j
           son-3.10.5-gbep6sj7r6o77skebrmynsdcs35kjx52/lib/cmake/nlohmann_json/nlohmann_jsonConfig.
           cmake (found suitable version "3.10.5", minimum required is "3.7.0")
     19    -- nlohmann-json: Found version 3.10.5
     20    -- Found HDF5: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/hdf5-1.12.2-godyvkc
           wlaxwahxwhmsquzba4l5vd6lx/lib/libhdf5.so;/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-
           11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/lib/libmpi.so (found suitable vers
           ion "1.12.2", minimum required is "1.8.13") found components: C
  >> 21    CMake Error at CMakeLists.txt:157 (message):
     22      Found MPI but only serial version of HDF5.  Either set openPMD_USE_MPI=OFF
     23      to disable MPI or set openPMD_USE_HDF5=OFF to disable HDF5 or provide a
     24      parallel install of HDF5.
     25    
     26    
     27    -- Configuring incomplete, errors occurred!
```


### superlu-dist: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package superlu-dist@5.0.0 --splice openmpi@master --runner spack --replace openmpi --experiment superlu-dist --outfile /results/superlu-dist/5.0.0/openmpi/experiment.json

==> [2022-07-28-20:47:45.434983, 11] 11: superlu-dist: Executing phase: 'build'
==> [2022-07-28-20:47:53.543632, 11] WRITE LOCK (spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k): /tmp/root/spack-stage/.lock[6505392650183886231:1] [Released at 20:47:53.543570] 
==> [2022-07-28-20:47:53.571369, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8'

33 errors found in build log:
     541    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack
            -stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-src/SRC -I/spack/opt/s
            pack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xyn
            rp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakb
            a5dfqwrw3xh7lbb7q7gz77sg/include -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 
            -std=c99 -O2 -g -DNDEBUG -MD -MT EXAMPLE/CMakeFiles/pddrive3.dir/dcreate_matrix.c.o -MF
             CMakeFiles/pddrive3.dir/dcreate_matrix.c.o.d -o CMakeFiles/pddrive3.dir/dcreate_matrix
            .c.o -c /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6
            goe72k/spack-src/EXAMPLE/dcreate_matrix.c
     542    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive1_ABglobal.dir/link.txt --verbose=1
     543    [ 74%] Linking C executable pddrive2_ABglobal
     544    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive2_ABglobal.dir/link.txt --verbose=1
     545    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive1_ABglobal.dir/pddrive1_ABglobal.c.o -o pd
            drive1_ABglobal  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/linux-ubuntu22.04-s
            kylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperl
            u_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4
            urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubuntu2
            2.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis 
            -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
            7lbb7q7gz77sg/lib -lmetis
     546    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive2_ABglobal.dir/pddrive2_ABglobal.c.o -o pd
            drive2_ABglobal  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/linux-ubuntu22.04-s
            kylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperl
            u_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4
            urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubuntu2
            2.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis 
            -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
            7lbb7q7gz77sg/lib -lmetis
  >> 547    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 548    collect2: error: ld returned 1 exit status
  >> 549    make[2]: *** [EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/build.make:102: EXAMPLE/pddrive_A
            Bglobal] Error 1
     550    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 551    make[1]: *** [CMakeFiles/Makefile2:313: EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/all] Er
            ror 2
     552    make[1]: *** Waiting for unfinished jobs....
     553    [ 75%] Linking C executable pddrive4
     554    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive4.dir/link.txt --verbose=1
  >> 555    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 556    collect2: error: ld returned 1 exit status
     557    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive4.dir/pddrive4.c.o CMakeFiles/pddrive4.dir
            /dcreate_matrix.c.o -o pddrive4  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 558    make[2]: *** [EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/build.make:102: EXAMPLE/pddrive1
            _ABglobal] Error 1
     559    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 560    make[1]: *** [CMakeFiles/Makefile2:339: EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/all] E
            rror 2
     561    [ 76%] Linking C executable pddrive
     562    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive.dir/link.txt --verbose=1
     563    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive.dir/pddrive.c.o CMakeFiles/pddrive.dir/dc
            reate_matrix.c.o -o pddrive  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-
            5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/linux-u
            buntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../S
            RC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openb
            las-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/l
            inux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib
             -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxak
            ba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     564    [ 77%] Linking C executable pddrive2
     565    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive2.dir/link.txt --verbose=1
     566    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive2.dir/pddrive2.c.o CMakeFiles/pddrive2.dir
            /dcreate_matrix.c.o -o pddrive2  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     567    [ 78%] Linking C executable pddrive3
     568    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive3.dir/link.txt --verbose=1
  >> 569    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 570    collect2: error: ld returned 1 exit status
     571    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive3.dir/pddrive3.c.o CMakeFiles/pddrive3.dir
            /dcreate_matrix.c.o -o pddrive3  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 572    make[2]: *** [EXAMPLE/CMakeFiles/pddrive2_ABglobal.dir/build.make:102: EXAMPLE/pddrive2
            _ABglobal] Error 1
     573    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 574    make[1]: *** [CMakeFiles/Makefile2:365: EXAMPLE/CMakeFiles/pddrive2_ABglobal.dir/all] E
            rror 2
     575    [ 79%] Linking C executable pddrive1
     576    cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72
            k/spack-build-thc3swy/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
            cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
            /pddrive1.dir/link.txt --verbose=1
     577    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioid
            lwxm2oeyqso4b/bin/mpicc  -DUSE_VENDOR_BLAS -DAdd_ -DDEBUGlevel=0 -DPRNTlevel=0 -std=c99
             -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive1.dir/pddrive1.c.o CMakeFiles/pddrive1.dir
            /dcreate_matrix.c.o -o pddrive1  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-d
            ist-5.0.0-thc3swy42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy/SRC:/spack/opt/spack/lin
            ux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib 
            ../SRC/libsuperlu_dist.so.5.0.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
            penblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spa
            ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp
            /lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77o
            rxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 578    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 579    collect2: error: ld returned 1 exit status
  >> 580    make[2]: *** [EXAMPLE/CMakeFiles/pddrive4.dir/build.make:118: EXAMPLE/pddrive4] Error 1
     581    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 582    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 583    make[1]: *** [CMakeFiles/Makefile2:287: EXAMPLE/CMakeFiles/pddrive4.dir/all] Error 2
  >> 584    collect2: error: ld returned 1 exit status
  >> 585    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 586    make[2]: *** [EXAMPLE/CMakeFiles/pddrive.dir/build.make:118: EXAMPLE/pddrive] Error 1
     587    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 588    make[1]: *** [CMakeFiles/Makefile2:183: EXAMPLE/CMakeFiles/pddrive.dir/all] Error 2
  >> 589    collect2: error: ld returned 1 exit status
  >> 590    make[2]: *** [EXAMPLE/CMakeFiles/pddrive2.dir/build.make:118: EXAMPLE/pddrive2] Error 1
     591    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 592    make[1]: *** [CMakeFiles/Makefile2:235: EXAMPLE/CMakeFiles/pddrive2.dir/all] Error 2
  >> 593    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 594    collect2: error: ld returned 1 exit status
  >> 595    make[2]: *** [EXAMPLE/CMakeFiles/pddrive3.dir/build.make:118: EXAMPLE/pddrive3] Error 1
     596    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 597    make[1]: *** [CMakeFiles/Makefile2:261: EXAMPLE/CMakeFiles/pddrive3.dir/all] Error 2
  >> 598    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urm
            se2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_conc
            at_string'
  >> 599    collect2: error: ld returned 1 exit status
  >> 600    make[2]: *** [EXAMPLE/CMakeFiles/pddrive1.dir/build.make:118: EXAMPLE/pddrive1] Error 1
     601    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 602    make[1]: *** [CMakeFiles/Makefile2:209: EXAMPLE/CMakeFiles/pddrive1.dir/all] Error 2
     603    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.0.0-thc3sw
            y42kbc3jq2hxmxefgvf6goe72k/spack-build-thc3swy'
  >> 604    make: *** [Makefile:149: all] Error 2

See build log for details:

```

### heffte: UNKNOWN

yaksa is too big to build, so likely won't work in gh-actions, we could try later.

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package heffte@0.1 --splice openmpi --runner spack --replace openmpi@master --experiment heffte --outfile /results/heffte/0.1/openmpi/experiment.json
```

### py-libensemble: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package py-libensemble@0.1.0 --splice py-numpy --runner spack --replace py-numpy --experiment py-libensemble --outfile /results/py-libensemble/0.1.0/py-numpy/experiment.json

==> [2022-07-28-21:15:00.731337, 1] Creating stage lock spack-stage-py-libensemble-0.1.0-vwee7waskhtn2eozzj2jqwupyje4t43v
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/spliced/experiment/spack.py", line 127, in do_install
    spec.package.do_install(force=True)
  File "/spack/lib/spack/spack/package_base.py", line 1905, in do_install
    builder.install()
  File "/spack/lib/spack/spack/installer.py", line 1699, in install
    self._install_task(task)
  File "/spack/lib/spack/spack/installer.py", line 1233, in _install_task
    spack.build_environment.start_build_process(
  File "/spack/lib/spack/spack/build_environment.py", line 1200, in start_build_process
    raise child_result
spack.build_environment.ChildError: OSError: No such file or directory: '/tmp/root/spack-stage/spack-stage-py-libensemble-0.1.0-vwee7waskhtn2eozzj2jqwupyje4t43v/spack-src/examples/calling_scripts/regression_tests'
```

### py-petsc4py: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package py-petsc4py@3.10.0 --splice py-mpi4py --runner spack --replace py-mpi4py --experiment py-petsc4py --outfile /results/py-petsc4py/3.10.0/py-mpi4py/experiment.json

==> [2022-07-28-21:16:31.238227, 73] 73: superlu-dist: Executing phase: 'build'
==> [2022-07-28-21:16:45.369010, 73] WRITE LOCK (spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73): /tmp/root/spack-stage/.lock[1936176548018551543:1] [Released at 21:16:45.368965] 
==> [2022-07-28-21:16:45.391703, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8'

33 errors found in build log:
     934     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/sp
             ack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC 
             -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg
             5x4iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/meti
             s-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-s
             uperlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/includ
             e -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnj
             kg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT EXAMPL
             E/CMakeFiles/pddrive2.dir/dcreate_matrix.c.o -MF CMakeFiles/pddrive2.dir/dcreate_matri
             x.c.o.d -o CMakeFiles/pddrive2.dir/dcreate_matrix.c.o -c /tmp/root/spack-stage/spack-s
             tage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/EXAMPLE/dcreate_mat
             rix.c
     935     [ 82%] Linking C executable pddrive1_ABglobal
     936     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive1_ABglobal.dir/link.txt --verbose=1
     937     [ 82%] Building C object EXAMPLE/CMakeFiles/pddrive3.dir/dcreate_matrix.c.o
     938     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/sp
             ack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC 
             -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg
             5x4iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/meti
             s-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-s
             uperlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/includ
             e -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnj
             kg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT EXAMPL
             E/CMakeFiles/pddrive3.dir/dcreate_matrix.c.o -MF CMakeFiles/pddrive3.dir/dcreate_matri
             x.c.o.d -o CMakeFiles/pddrive3.dir/dcreate_matrix.c.o -c /tmp/root/spack-stage/spack-s
             tage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/EXAMPLE/dcreate_mat
             rix.c
     939     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive1_ABglobal.dir/pddrive1_AB
             global.c.o -o pddrive1_ABglobal  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-
             dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/spack/opt/spack/l
             inux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/l
             ib ../SRC/libsuperlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2
             .0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/op
             t/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi
             6xynrp/lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.
             1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 940     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 941     collect2: error: ld returned 1 exit status
  >> 942     make[2]: *** [EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/build.make:102: EXAMPLE/pddrive_
             ABglobal] Error 1
     943     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
     944     [ 82%] Building C object TEST/CMakeFiles/pdtest.dir/dcreate_matrix.c.o
  >> 945     make[1]: *** [CMakeFiles/Makefile2:385: EXAMPLE/CMakeFiles/pddrive_ABglobal.dir/all] E
             rror 2
     946     make[1]: *** Waiting for unfinished jobs....
     947     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/TEST && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
             penmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC -I/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4
             iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5
             .1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/linux
             -ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -
             I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5
             x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT TEST/CMak
             eFiles/pdtest.dir/dcreate_matrix.c.o -MF CMakeFiles/pdtest.dir/dcreate_matrix.c.o.d -o
              CMakeFiles/pdtest.dir/dcreate_matrix.c.o -c /tmp/root/spack-stage/spack-stage-superlu
             -dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/TEST/dcreate_matrix.c
     948     [ 83%] Building C object TEST/CMakeFiles/pdtest.dir/pdcompute_resid.c.o
     949     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/TEST && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/o
             penmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC -I/
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4
             iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5
             .1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/linux
             -ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -
             I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5
             x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT TEST/CMak
             eFiles/pdtest.dir/pdcompute_resid.c.o -MF CMakeFiles/pdtest.dir/pdcompute_resid.c.o.d 
             -o CMakeFiles/pdtest.dir/pdcompute_resid.c.o -c /tmp/root/spack-stage/spack-stage-supe
             rlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/TEST/pdcompute_resid.c
  >> 950     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 951     collect2: error: ld returned 1 exit status
  >> 952     make[2]: *** [EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/build.make:102: EXAMPLE/pddrive
             1_ABglobal] Error 1
     953     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 954     make[1]: *** [CMakeFiles/Makefile2:411: EXAMPLE/CMakeFiles/pddrive1_ABglobal.dir/all] 
             Error 2
     955     [ 83%] Building C object EXAMPLE/CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o
     956     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/sp
             ack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC 
             -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg
             5x4iik7s4hi6xynrp/include -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/meti
             s-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack-stage-s
             uperlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-src/SRC -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/includ
             e -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnj
             kg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -MD -MT EXAMPL
             E/CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o -MF CMakeFiles/pddrive2.dir/dcr
             eate_matrix_perturbed.c.o.d -o CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o -c
              /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73
             /spack-src/EXAMPLE/dcreate_matrix_perturbed.c
     957     [ 84%] Linking C executable pddrive4
     958     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive4.dir/link.txt --verbose=1
     959     [ 84%] Linking C executable pddrive1
     960     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive1.dir/link.txt --verbose=1

     ...

     965     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive.dir/pddrive.c.o CMakeFile
             s/pddrive.dir/dcreate_matrix.c.o -o pddrive  -Wl,-rpath,/tmp/root/spack-stage/spack-st
             age-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/spack
             /opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax
             4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-skyl
             ake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm
              -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjk
             g5x4iik7s4hi6xynrp/lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.
             2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     966     [ 86%] Linking C executable pddrive3
     967     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive3.dir/link.txt --verbose=1
     968     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive3.dir/pddrive3.c.o CMakeFi
             les/pddrive3.dir/dcreate_matrix.c.o -o pddrive3  -Wl,-rpath,/tmp/root/spack-stage/spac
             k-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/s
             pack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuq
             vsax4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so
              -lm -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3
             lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc
             -11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     969     [ 86%] Linking C executable pdtest
     970     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/TEST && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/c
             make-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles
             /pdtest.dir/link.txt --verbose=1
  >> 971     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
     972     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pdtest.dir/pdtest.c.o CMakeFiles/
             pdtest.dir/dcreate_matrix.c.o CMakeFiles/pdtest.dir/pdcompute_resid.c.o -o pdtest  -Wl
             ,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjj
             w3wdb73/spack-build-atky62e/SRC:/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/
             openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.5.4.0 /
             spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihu
             qvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubuntu22.04-skylake/gc
             c-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg
             /lib -lmetis
  >> 973     collect2: error: ld returned 1 exit status
  >> 974     make[2]: *** [EXAMPLE/CMakeFiles/pddrive4.dir/build.make:118: EXAMPLE/pddrive4] Error 
             1
     975     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 976     make[1]: *** [CMakeFiles/Makefile2:359: EXAMPLE/CMakeFiles/pddrive4.dir/all] Error 2
  >> 977     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 978     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 979     collect2: error: ld returned 1 exit status
  >> 980     make[2]: *** [EXAMPLE/CMakeFiles/pddrive1.dir/build.make:118: EXAMPLE/pddrive1] Error 
             1
     981     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 982     make[1]: *** [CMakeFiles/Makefile2:281: EXAMPLE/CMakeFiles/pddrive1.dir/all] Error 2
  >> 983     collect2: error: ld returned 1 exit status
  >> 984     make[2]: *** [EXAMPLE/CMakeFiles/pddrive.dir/build.make:118: EXAMPLE/pddrive] Error 1
     985     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 986     make[1]: *** [CMakeFiles/Makefile2:255: EXAMPLE/CMakeFiles/pddrive.dir/all] Error 2
  >> 987     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 988     collect2: error: ld returned 1 exit status
  >> 989     make[2]: *** [EXAMPLE/CMakeFiles/pddrive3.dir/build.make:118: EXAMPLE/pddrive3] Error 
             1
     990     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 991     make[1]: *** [CMakeFiles/Makefile2:333: EXAMPLE/CMakeFiles/pddrive3.dir/all] Error 2
     992     [ 87%] Linking C executable pddrive2
     993     cd /tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62eev3jnculrxgo2mrgjjw3wdb
             73/spack-build-atky62e/EXAMPLE && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.
             0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFi
             les/pddrive2.dir/link.txt --verbose=1
     994     /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioi
             dlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis
             -5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR
             _BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles/pddrive2.dir/pddrive2.c.o CMakeFi
             les/pddrive2.dir/dcreate_matrix.c.o CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c
             .o -o pddrive2  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky62
             eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e/SRC:/spack/opt/spack/linux-ubuntu22.04-
             skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsupe
             rlu_dist.so.5.4.0 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.2
             0-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-ubu
             ntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparm
             etis -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfq
             wrw3xh7lbb7q7gz77sg/lib -lmetis
  >> 995     /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 996     collect2: error: ld returned 1 exit status
  >> 997     make[2]: *** [TEST/CMakeFiles/pdtest.dir/build.make:134: TEST/pdtest] Error 1
     998     make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 999     make[1]: *** [CMakeFiles/Makefile2:229: TEST/CMakeFiles/pdtest.dir/all] Error 2
  >> 1000    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so: undefined reference to `_gfortran_co
             ncat_string'
  >> 1001    collect2: error: ld returned 1 exit status
  >> 1002    make[2]: *** [EXAMPLE/CMakeFiles/pddrive2.dir/build.make:134: EXAMPLE/pddrive2] Error 
             1
     1003    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 1004    make[1]: *** [CMakeFiles/Makefile2:307: EXAMPLE/CMakeFiles/pddrive2.dir/all] Error 2
     1005    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-superlu-dist-5.4.0-atky6
             2eev3jnculrxgo2mrgjjw3wdb73/spack-build-atky62e'
  >> 1006    make: *** [Makefile:149: all] Error 2

```

### parsec: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package parsec@1.1.0 --splice openmpi@master --runner spack --replace openmpi --experiment parsec --outfile /results/parsec/1.1.0/openmpi/experiment.json

EC_DEBUG_HISTORY:BOOL=OFF' '-DPARSEC_DEBUG_PARANOID:BOOL=OFF' '/tmp/root/spack-stage/spack-stage-parsec-1.1.0-ucbyzk7c3mi6rhwueo37qgqwhujeregn/spack-src'

1 error found in build log:
     142    -- Could NOT find Omega; Options depending on Omega will be disabled
     143      if needed, please specify the library location
     144        - using OMEGA_DIR []
     145        - or a combination of OMEGA_INCLUDE_DIR [OMEGA_INCLUDE_DIR-NOTFOUND] and OMEGA_LIBR
            ARY [OMEGA_LIBRARY-NOTFOUND] (missing: OMEGA_INCLUDE_DIR OMEGA_LIBRARY)
     146    -- Generate precision dependencies in /tmp/root/spack-stage/spack-stage-parsec-1.1.0-uc
            byzk7c3mi6rhwueo37qgqwhujeregn/spack-src/data_dist/matrix
     147    -- Generate precision dependencies in /tmp/root/spack-stage/spack-stage-parsec-1.1.0-uc
            byzk7c3mi6rhwueo37qgqwhujeregn/spack-src/data_dist/matrix - Done
  >> 148    CMake Error at cmake_modules/FindCOREBLAS.cmake:109 (else):
     149      Flow control statements are not properly nested.
     150    Call Stack (most recent call first):
     151      dplasma/CMakeLists.txt:25 (find_package)
     152    
     153    
     154    CMake Warning at dplasma/CMakeLists.txt:25 (find_package):
```

### raja: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package raja@0.10.0 --splice blt@master --runner spack --replace blt --experiment raja --outfile /results/raja/0.10.0/blt/experiment.json
```

yay!

### caliper: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package caliper@1.7.0 --splice papi@master --runner spack --replace papi --experiment caliper --outfile /results/caliper/1.7.0/papi/experiment.json


==> [2022-07-28-21:44:30.787085, 3136] WRITE LOCK (spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c): /tmp/root/spack-stage/.lock[2044469360343817241:1] [Released at 21:44:30.787040] 
==> [2022-07-28-21:44:30.802841, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8'

5 errors found in build log:
     369    [ 37%] Built target caliper-sampler
     370    [ 37%] Building CXX object mpi/mpi-rt/services/mpiwrap/CMakeFiles/caliper-mpiwrap.dir/M
            piWrap.cpp.o
     371    cd /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spa
            ck-build-jruzdqi/mpi/mpi-rt/services/mpiwrap && /spack/lib/spack/env/gcc/g++  -I/tmp/ro
            ot/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-build-j
            ruzdqi/include -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajm
            ctuzhhai2c/spack-src/include -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6
            t2yiadasqbpajmctuzhhai2c/spack-src/mpi/include -I/spack/opt/spack/linux-ubuntu22.04-sky
            lake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/include -I/tmp/root/spac
            k-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-src/mpi/mpi-rt
             -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spa
            ck-build-jruzdqi/ext/gotcha/gotcha-download/gotcha-src/include -O2 -g -DNDEBUG -fPIC -s
            td=gnu++11 -MD -MT mpi/mpi-rt/services/mpiwrap/CMakeFiles/caliper-mpiwrap.dir/MpiWrap.c
            pp.o -MF CMakeFiles/caliper-mpiwrap.dir/MpiWrap.cpp.o.d -o CMakeFiles/caliper-mpiwrap.d
            ir/MpiWrap.cpp.o -c /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbp
            ajmctuzhhai2c/spack-src/mpi/mpi-rt/services/mpiwrap/MpiWrap.cpp
     372    [ 37%] Linking C executable autotee_test
     373    cd /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spa
            ck-build-jruzdqi/ext/gotcha/gotcha-download/gotcha-build/src/example/autotee && /spack/
            opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r
            5pc5m/bin/cmake -E cmake_link_script CMakeFiles/autotee_test.dir/link.txt --verbose=1
     374    /spack/lib/spack/env/gcc/gcc -O2 -g -DNDEBUG -rdynamic CMakeFiles/autotee_test.dir/test
            _autotee.c.o -o autotee_test  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-caliper-1.7.
            0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-build-jruzdqi/ext/gotcha/gotcha-download/gotch
            a-build/src/example/autotee:/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2y
            iadasqbpajmctuzhhai2c/spack-build-jruzdqi/ext/gotcha/gotcha-download/gotcha-build/src l
            ibautotee.so ../../libgotcha.so.1.0.1
  >> 375    /usr/bin/ld: ../../libgotcha.so.1.0.1: undefined reference to `_dl_sym'
  >> 376    collect2: error: ld returned 1 exit status
  >> 377    make[2]: *** [ext/gotcha/gotcha-download/gotcha-build/src/example/autotee/CMakeFiles/au
            totee_test.dir/build.make:102: ext/gotcha/gotcha-download/gotcha-build/src/example/auto
            tee/autotee_test] Error 1
     378    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2y
            iadasqbpajmctuzhhai2c/spack-build-jruzdqi'
  >> 379    make[1]: *** [CMakeFiles/Makefile2:1012: ext/gotcha/gotcha-download/gotcha-build/src/ex
            ample/autotee/CMakeFiles/autotee_test.dir/all] Error 2
     380    make[1]: *** Waiting for unfinished jobs....
     381    [ 37%] Building CXX object src/services/CMakeFiles/caliper-services.dir/env/Environment
            Info.cpp.o
     382    cd /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spa
            ck-build-jruzdqi/src/services && /spack/lib/spack/env/gcc/g++  -I/tmp/root/spack-stage/
            spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-build-jruzdqi/include 
            -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spac
            k-src/include -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmc
            tuzhhai2c/spack-build-jruzdqi -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi
            6t2yiadasqbpajmctuzhhai2c/spack-src/src -I/tmp/root/spack-stage/spack-stage-caliper-1.7
            .0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-build-jruzdqi/src/services -O2 -g -DNDEBUG -f
            PIC -std=gnu++11 -MD -MT src/services/CMakeFiles/caliper-services.dir/env/EnvironmentIn
            fo.cpp.o -MF CMakeFiles/caliper-services.dir/env/EnvironmentInfo.cpp.o.d -o CMakeFiles/
            caliper-services.dir/env/EnvironmentInfo.cpp.o -c /tmp/root/spack-stage/spack-stage-cal
            iper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-src/src/services/env/EnvironmentInfo.
            cpp
     383    [ 38%] Building CXX object src/common/CMakeFiles/caliper-common.dir/CaliperMetadataAcce
            ssInterface.cpp.o
     384    cd /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spa
            ck-build-jruzdqi/src/common && /spack/lib/spack/env/gcc/g++ -Dcaliper_common_EXPORTS -I
            /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-
            build-jruzdqi/include -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiada
            sqbpajmctuzhhai2c/spack-src/include -I/tmp/root/spack-stage/spack-stage-caliper-1.7.0-j
            ruzdqi6t2yiadasqbpajmctuzhhai2c/spack-build-jruzdqi -I/tmp/root/spack-stage/spack-stage
            -caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-src/src -O2 -g -DNDEBUG -fPIC -st
            d=gnu++11 -MD -MT src/common/CMakeFiles/caliper-common.dir/CaliperMetadataAccessInterfa
            ce.cpp.o -MF CMakeFiles/caliper-common.dir/CaliperMetadataAccessInterface.cpp.o.d -o CM
            akeFiles/caliper-common.dir/CaliperMetadataAccessInterface.cpp.o -c /tmp/root/spack-sta
            ge/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spack-src/src/common/Cali
            perMetadataAccessInterface.cpp
     385    [ 40%] Building CXX object mpi/mpi-rt/services/mpiwrap/CMakeFiles/caliper-mpiwrap.dir/W
            rapper.cpp.o

     ...

     677    cd /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spa
            ck-build-jruzdqi/src/common && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/cm
            ake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles/c
            aliper-common.dir/link.txt --verbose=1
     678    /spack/lib/spack/env/gcc/g++ -fPIC -O2 -g -DNDEBUG -shared -Wl,-soname,libcaliper-commo
            n.so.1 -o libcaliper-common.so.1.7.0 "CMakeFiles/caliper-common.dir/Attribute.cpp.o" "C
            MakeFiles/caliper-common.dir/CaliperMetadataAccessInterface.cpp.o" "CMakeFiles/caliper-
            common.dir/CompressedSnapshotRecord.cpp.o" "CMakeFiles/caliper-common.dir/ContextRecord
            .cpp.o" "CMakeFiles/caliper-common.dir/Entry.cpp.o" "CMakeFiles/caliper-common.dir/Log.
            cpp.o" "CMakeFiles/caliper-common.dir/Node.cpp.o" "CMakeFiles/caliper-common.dir/NodeBu
            ffer.cpp.o" "CMakeFiles/caliper-common.dir/OutputStream.cpp.o" "CMakeFiles/caliper-comm
            on.dir/RecordMap.cpp.o" "CMakeFiles/caliper-common.dir/RuntimeConfig.cpp.o" "CMakeFiles
            /caliper-common.dir/SnapshotBuffer.cpp.o" "CMakeFiles/caliper-common.dir/SnapshotTextFo
            rmatter.cpp.o" "CMakeFiles/caliper-common.dir/StringConverter.cpp.o" "CMakeFiles/calipe
            r-common.dir/Variant.cpp.o" "CMakeFiles/caliper-common.dir/cali_types.c.o" "CMakeFiles/
            caliper-common.dir/cali_variant.c.o" "csv/CMakeFiles/caliper-csv.dir/CsvReader.cpp.o" "
            csv/CMakeFiles/caliper-csv.dir/CsvSpec.cpp.o" "csv/CMakeFiles/caliper-csv.dir/CsvWriter
            .cpp.o" "c-util/CMakeFiles/c-util.dir/unitfmt.c.o" "c-util/CMakeFiles/c-util.dir/vlenc.
            c.o" util/CMakeFiles/util.dir/parse_util.cpp.o  -Wl,-rpath,::::::::::::::::::::::::::::
            ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
     679    cd /tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2yiadasqbpajmctuzhhai2c/spa
            ck-build-jruzdqi/src/common && /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/cm
            ake-3.23.2-pmpcgqf26kzzlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_symlink_library libcalip
            er-common.so.1.7.0 libcaliper-common.so.1 libcaliper-common.so
     680    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2y
            iadasqbpajmctuzhhai2c/spack-build-jruzdqi'
     681    [ 64%] Built target caliper-common
     682    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-caliper-1.7.0-jruzdqi6t2y
            iadasqbpajmctuzhhai2c/spack-build-jruzdqi'
  >> 683    make: *** [Makefile:139: all] Error 2

```

### nrm: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package nrm@0.1.0 --splice py-jsonschema --runner spack --replace py-jsonschema --experiment nrm --outfile /results/nrm/0.1.0/py-jsonschema/experiment.json
```

nrm build failed (can't find obvious traceback).

### upcxx: UNKNOWN

Splice failed, but other variants might work (should try)

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package upcxx@2020.10.0 --splice python@3.8.1 --runner spack --replace python --experiment upcxx --outfile /results/upcxx/2020.10.0/python/experiment.json
```

### arborx: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package arborx@1.0 --splice openmpi --runner spack --replace openmpi --experiment arborx --outfile /results/arborx/1.0/openmpi/experiment.json
```

### ginkgo: UNKNOWN

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package ginkgo@1.0.0 --splice cmake --runner spack --replace cmake --experiment ginkgo --outfile /results/ginkgo/1.0.0/cmake/experiment.json
```

It took too long to run with cmake so we should test it.

### legion: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package legion@21.03.0 --splice zlib --runner spack --replace zlib --experiment legion --outfile /results/legion/21.03.0/zlib/experiment.json
```

### py-jupyterhub:  FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package py-jupyterhub@0.9.4 --splice py-certipy --runner spack --replace py-certipy --experiment py-jupyterhub --outfile /results/py-jupyterhub/0.9.4/py-certipy/experiment.json
```

Don't have terminal, mine crashed when I was scrolling up, but the base install definitely failed!
(I saw the message at the bottom).

### bolt: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package bolt@1.0 --splice argobots --runner spack --replace argobots --experiment bolt --outfile /results/bolt/1.0/argobots/experiment.json
```

### aml: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package aml@0.1.0 --splice numactl --runner spack --replace numactl --experiment aml --outfile /results/aml/0.1.0/numactl/experiment.json


     161    checking numa.h presence... yes
     162    checking for numa.h... yes
     163    checking numaif.h usability... yes
     164    checking numaif.h presence... yes
     165    checking for numaif.h... yes
     166    checking for mbind in -lnuma... yes
  >> 167    /tmp/root/spack-stage/spack-stage-aml-master-fyq7osgx6tqvk6gre5jq3x
            abtbqqdwac/spack-src/configure: line 15056: syntax error near unexp
            ected token `HWLOC,hwloc'
     168    /tmp/root/spack-stage/spack-stage-aml-master-fyq7osgx6tqvk6gre5jq3x
            abtbqqdwac/spack-src/configure: line 15056: `PKG_HAVE_WITH_MODULES(
            HWLOC,hwloc >= 2.1,,)'
```

This failed for both versions of numactl [ref](https://github.com/buildsi/splice-experiment-runs/runs/7566167498?check_suite_focus=true).

### openmpi: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package openmpi@1.0 --splice pkgconf --runner spack --replace pkgconf@1.8.0 --experiment openmpi --outfile /results/openmpi/1.0/pkgconf/experiment.json

...

  >> 16843    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (LOGICAL(16)/LOGICAL(1)).
     16844    mpi_bsend_init_f90.f90:807:22:
     16845    
     16846       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16847          |                      2
     16848    ......
     16849      807 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16850          |                      1
  >> 16851    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(1)/LOGICAL(1)).
     16852    mpi_bsend_init_f90.f90:822:22:
     16853    
     16854       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16855          |                      2
     16856    ......
     16857      822 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16858          |                      1
  >> 16859    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(2)/LOGICAL(1)).
     16860    mpi_bsend_init_f90.f90:837:22:
     16861    
     16862       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16863          |                      2
     16864    ......
     16865      837 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16866          |                      1
  >> 16867    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(4)/LOGICAL(1)).
     16868    mpi_bsend_init_f90.f90:852:22:
     16869    
     16870       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16871          |                      2
     16872    ......
     16873      852 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16874          |                      1
  >> 16875    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(8)/LOGICAL(1)).
     16876    mpi_bsend_init_f90.f90:867:22:
     16877    
     16878       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16879          |                      2
     16880    ......
     16881      867 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16882          |                      1
  >> 16883    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(16)/LOGICAL(1)).
     16884    mpi_bsend_init_f90.f90:882:22:
     16885    
     16886       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16887          |                      2
     16888    ......
     16889      882 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16890          |                      1
  >> 16891    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (REAL(4)/LOGICAL(1)).
     16892    mpi_bsend_init_f90.f90:897:22:
     16893    
     16894       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16895          |                      2
     16896    ......
     16897      897 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16898          |                      1
  >> 16899    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (REAL(8)/LOGICAL(1)).
     16900    mpi_bsend_init_f90.f90:912:22:
     16901    
     16902       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16903          |                      2
     16904    ......
     16905      912 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16906          |                      1
  >> 16907    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (REAL(16)/LOGICAL(1)).
     16908    mpi_bsend_init_f90.f90:927:22:
     16909    
     16910       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16911          |                      2
     16912    ......
     16913      927 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16914          |                      1
  >> 16915    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (COMPLEX(4)/LOGICAL(1)).
     16916    mpi_bsend_init_f90.f90:942:22:
     16917    
     16918       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16919          |                      2
     16920    ......
     16921      942 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16922          |                      1
  >> 16923    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (COMPLEX(8)/LOGICAL(1)).
     16924    mpi_bsend_init_f90.f90:957:22:
     16925    
     16926       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16927          |                      2
     16928    ......
     16929      957 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16930          |                      1
  >> 16931    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (COMPLEX(16)/LOGICAL(1)).
     16932    mpi_bsend_init_f90.f90:972:22:
     16933    
     16934       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16935          |                      2
     16936    ......
     16937      972 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16938          |                      1
  >> 16939    Error: Rank mismatch between actual argument at (1) and actual ar
              gument at (2) (scalar and rank-4)
     16940    mpi_bsend_init_f90.f90:987:22:
     16941    
     16942       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16943          |                      2
     16944    ......
     16945      987 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16946          |                      1
  >> 16947    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (LOGICAL(2)/LOGICAL(1)).
     16948    mpi_bsend_init_f90.f90:1002:22:
     16949    
     16950       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16951          |                      2
     16952    ......
     16953     1002 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16954          |                      1
  >> 16955    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (LOGICAL(4)/LOGICAL(1)).
     16956    mpi_bsend_init_f90.f90:1017:22:
     16957    
     16958       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16959          |                      2
     16960    ......
     16961     1017 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16962          |                      1
  >> 16963    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (LOGICAL(8)/LOGICAL(1)).
     16964    mpi_bsend_init_f90.f90:1032:22:
     16965    
     16966       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16967          |                      2
     16968    ......
     16969     1032 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16970          |                      1
  >> 16971    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (LOGICAL(16)/LOGICAL(1)).
     16972    mpi_bsend_init_f90.f90:1047:22:
     16973    
     16974       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16975          |                      2
     16976    ......
     16977     1047 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16978          |                      1
  >> 16979    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(1)/LOGICAL(1)).
     16980    mpi_bsend_init_f90.f90:1062:22:
     16981    
     16982       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16983          |                      2
     16984    ......
     16985     1062 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16986          |                      1
  >> 16987    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(2)/LOGICAL(1)).
     16988    mpi_bsend_init_f90.f90:1077:22:
     16989    
     16990       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16991          |                      2
     16992    ......
     16993     1077 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16994          |                      1
  >> 16995    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(4)/LOGICAL(1)).
     16996    mpi_bsend_init_f90.f90:1092:22:
     16997    
     16998       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     16999          |                      2
     17000    ......
     17001     1092 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17002          |                      1
  >> 17003    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(8)/LOGICAL(1)).
     17004    mpi_bsend_init_f90.f90:1107:22:
     17005    
     17006       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17007          |                      2
     17008    ......
     17009     1107 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17010          |                      1
  >> 17011    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (INTEGER(16)/LOGICAL(1)).
     17012    mpi_bsend_init_f90.f90:1122:22:
     17013    
     17014       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17015          |                      2
     17016    ......
     17017     1122 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17018          |                      1
  >> 17019    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (REAL(4)/LOGICAL(1)).
     17020    mpi_bsend_init_f90.f90:1137:22:
     17021    
     17022       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17023          |                      2
     17024    ......
     17025     1137 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17026          |                      1
  >> 17027    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (REAL(8)/LOGICAL(1)).
     17028    mpi_bsend_init_f90.f90:1152:22:
     17029    
     17030       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17031          |                      2
     17032    ......
     17033     1152 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17034          |                      1
  >> 17035    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (REAL(16)/LOGICAL(1)).
     17036    mpi_bsend_init_f90.f90:1167:22:
     17037    
     17038       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17039          |                      2
     17040    ......
     17041     1167 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17042          |                      1
  >> 17043    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (COMPLEX(4)/LOGICAL(1)).
     17044    mpi_bsend_init_f90.f90:1182:22:
     17045    
     17046       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17047          |                      2
     17048    ......
     17049     1182 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17050          |                      1
  >> 17051    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (COMPLEX(8)/LOGICAL(1)).
     17052    mpi_bsend_init_f90.f90:1197:22:
     17053    
     17054       12 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17055          |                      2
     17056    ......
     17057     1197 |   call MPI_Bsend_init(buf, count, datatype, dest, tag, &
     17058          |                      1
  >> 17059    Error: Type mismatch between actual argument at (1) and actual ar
              gument at (2) (COMPLEX(16)/LOGICAL(1)).
  >> 17060    make[5]: *** [Makefile:1346: mpi_bsend_init_f90.o] Error 1
     17061    Finished generating Fortran 90 interface functions
     17062    make[5]: Leaving directory '/tmp/root/spack-stage/spack-stage-ope
              nmpi-1.0-k7nwdvhnw7bfh4kgsljqu2rrjxi3ovru/spack-src/ompi/mpi/f90'
  >> 17063    make[4]: *** [Makefile:1065: all-recursive] Error 1
     17064    make[4]: Leaving directory '/tmp/root/spack-stage/spack-stage-ope
              nmpi-1.0-k7nwdvhnw7bfh4kgsljqu2rrjxi3ovru/spack-src/ompi/mpi/f90'
  >> 17065    make[3]: *** [Makefile:971: all] Error 2
     17066    make[3]: Leaving directory '/tmp/root/spack-stage/spack-stage-ope
              nmpi-1.0-k7nwdvhnw7bfh4kgsljqu2rrjxi3ovru/spack-src/ompi/mpi/f90'
  >> 17067    make[2]: *** [Makefile:843: all-recursive] Error 1
     17068    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-ope
              nmpi-1.0-k7nwdvhnw7bfh4kgsljqu2rrjxi3ovru/spack-src/ompi/mpi'
  >> 17069    make[1]: *** [Makefile:1022: all-recursive] Error 1
     17070    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-ope
              nmpi-1.0-k7nwdvhnw7bfh4kgsljqu2rrjxi3ovru/spack-src/ompi'
  >> 17071    make: *** [Makefile:864: all-recursive] Error 1

...
```

### parallel-netcdf: FAIL

If openmpi (above) doesn't work, this won't either

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package parallel-netcdf@1.10.0 --splice openmpi --runner spack --replace openmpi --experiment parallel-netcdf --outfile /results/parallel-netcdf/1.10.0/openmpi/experiment.json
```

### superlu: SUCCESS

I think it installed but I missed the success message (it was streaming too fast) so I'm going to run it.

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package superlu@5.2.1 --splice openblas --runner spack --replace openblas --experiment superlu --outfile /results/superlu/5.2.1/openblas/experiment.json
```

### mfem: FAIL

Requires openmpi, won't work

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package mfem@3.1 --splice openmpi --runner spack --replace openmpi --experiment mfem --outfile /results/mfem/3.1/openmpi/experiment.json
```

### hypre: FAIL

Requires openmpi, won't work

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package hypre@2.10.0b --splice openmpi --runner spack --replace openmpi --experiment hypre --outfile /results/hypre/2.10.0b/openmpi/experiment.json
```


### darshan-util: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package darshan-util@3.0.0 --splice zlib --runner spack --replace zlib --experiment darshan-util --outfile /results/darshan-util/3.0.0/zlib/experiment.json
```

### slepc: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package slepc@3.10.0 --splice petsc --runner spack --replace petsc@3.10.0 --experiment slepc --outfile /results/slepc/3.10.0/petsc/experiment.json

==> [2022-07-29-02:16:04.498408, 3688] 3688: superlu-dist: Executing phase: 'cmake'
==> [2022-07-29-02:16:06.561519, 3688] 3688: superlu-dist: Executing phase: 'build'
==> [2022-07-29-02:16:25.073894, 3688] WRITE LOCK (spack-stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa): /tmp/root/spack-stage/.lock[3701324042554369262:1] [Released at 02:16:25.073850] 
==> [2022-07-29-02:16:25.097558, 1] Error: ProcessError: Command exited with status 2:
    'make' '-j8'

21 errors found in build log:
     1100    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE && /spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjh
             sk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack-st
             age-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-buil
             d-k7rciud/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.
             2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -I/spa
             ck/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77or
             xakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-s
             rc/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/met
             is-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spa
             ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3l
             njkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -
             DNDEBUG -fPIE -MD -MT EXAMPLE/CMakeFiles/pddrive2.dir/pddrive2.c.o
              -MF CMakeFiles/pddrive2.dir/pddrive2.c.o.d -o CMakeFiles/pddrive2
             .dir/pddrive2.c.o -c /tmp/root/spack-stage/spack-stage-superlu-dis
             t-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-src/EXAMPLE/pddrive
             2.c
     1101    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.
             4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
             7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-skylake
             /gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/includ
             e -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles
             /pdtest.dir/pdtest.c.o CMakeFiles/pdtest.dir/dcreate_matrix.c.o CM
             akeFiles/pdtest.dir/pdcompute_resid.c.o -o pdtest  -Wl,-rpath,/tmp
             /root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatklrjnl2x
             laxa4l3jk4b2jxa/spack-build-k7rciud/SRC:/spack/opt/spack/linux-ubu
             ntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsihuqvsax
             4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.6.1.1 /spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4urmse2d27wawsi
             huqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spack/opt/spack/linux-
             ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4ii
             k7s4hi6xynrp/lib -lparmetis -L/spack/opt/spack/linux-ubuntu22.04-s
             kylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/lib
              -lmetis
     1102    [ 80%] Building C object EXAMPLE/CMakeFiles/pddrive1.dir/dcreate_m
             atrix.c.o
     1103    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE && /spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjh
             sk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack-st
             age-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-buil
             d-k7rciud/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.
             2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -I/spa
             ck/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77or
             xakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-s
             rc/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/met
             is-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spa
             ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3l
             njkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -
             DNDEBUG -fPIE -MD -MT EXAMPLE/CMakeFiles/pddrive1.dir/dcreate_matr
             ix.c.o -MF CMakeFiles/pddrive1.dir/dcreate_matrix.c.o.d -o CMakeFi
             les/pddrive1.dir/dcreate_matrix.c.o -c /tmp/root/spack-stage/spack
             -stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-s
             rc/EXAMPLE/dcreate_matrix.c
     1104    [ 81%] Building C object EXAMPLE/CMakeFiles/pddrive2.dir/dcreate_m
             atrix.c.o
     1105    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE && /spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjh
             sk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack-st
             age-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-buil
             d-k7rciud/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.
             2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -I/spa
             ck/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77or
             xakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-s
             rc/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/met
             is-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spa
             ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3l
             njkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -
             DNDEBUG -fPIE -MD -MT EXAMPLE/CMakeFiles/pddrive2.dir/dcreate_matr
             ix.c.o -MF CMakeFiles/pddrive2.dir/dcreate_matrix.c.o.d -o CMakeFi
             les/pddrive2.dir/dcreate_matrix.c.o -c /tmp/root/spack-stage/spack
             -stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-s
             rc/EXAMPLE/dcreate_matrix.c
  >> 1106    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0
             /openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.
             so: undefined reference to `_gfortran_concat_string'
     1107    [ 81%] Building C object EXAMPLE/CMakeFiles/pddrive2.dir/dcreate_m
             atrix_perturbed.c.o
  >> 1108    collect2: error: ld returned 1 exit status
  >> 1109    make[2]: *** [TEST/CMakeFiles/pdtest.dir/build.make:134: TEST/pdte
             st] Error 1
     1110    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE && /spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.4-cqmipy3bjh
             sk5dbioidlwxm2oeyqso4b/bin/mpicc  -I/tmp/root/spack-stage/spack-st
             age-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-buil
             d-k7rciud/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.
             2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/include -I/spa
             ck/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77or
             xakba5dfqwrw3xh7lbb7q7gz77sg/include -I/tmp/root/spack-stage/spack
             -stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-s
             rc/SRC -I/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/met
             is-5.1.0-77orxakba5dfqwrw3xh7lbb7q7gz77sg/include -I/spack/opt/spa
             ck/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3l
             njkg5x4iik7s4hi6xynrp/include -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -
             DNDEBUG -fPIE -MD -MT EXAMPLE/CMakeFiles/pddrive2.dir/dcreate_matr
             ix_perturbed.c.o -MF CMakeFiles/pddrive2.dir/dcreate_matrix_pertur
             bed.c.o.d -o CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o 
             -c /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-src/EXAMPLE/dcreate_matrix_perturbed.
             c
     1111    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
     1112    make  -f EXAMPLE/CMakeFiles/pddrive3.dir/build.make EXAMPLE/CMakeF
             iles/pddrive3.dir/depend
  >> 1113    make[1]: *** [CMakeFiles/Makefile2:229: TEST/CMakeFiles/pdtest.dir
             /all] Error 2
     1114    make[1]: *** Waiting for unfinished jobs....
     1115    make[2]: Entering directory '/tmp/root/spack-stage/spack-stage-sup
             erlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rci
             ud'
     1116    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud && /spack/opt/spack/lin
             ux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-pmpcgqf26kzzlogzxqh
             l47wva5r5pc5m/bin/cmake -E cmake_depends "Unix Makefiles" /tmp/roo
             t/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa
             4l3jk4b2jxa/spack-src /tmp/root/spack-stage/spack-stage-superlu-di
             st-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-src/EXAMPLE /tmp/r
             oot/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatklrjnl2xla
             xa4l3jk4b2jxa/spack-build-k7rciud /tmp/root/spack-stage/spack-stag
             e-superlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-
             k7rciud/EXAMPLE /tmp/root/spack-stage/spack-stage-superlu-dist-6.1
             .1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE/CM
             akeFiles/pddrive3.dir/DependInfo.cmake --color=
     1117    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
     1118    make  -f EXAMPLE/CMakeFiles/pddrive3.dir/build.make EXAMPLE/CMakeF
             iles/pddrive3.dir/build
     1119    make[2]: Entering directory '/tmp/root/spack-stage/spack-stage-sup
             erlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rci
             ud'

     ...

     1129    [ 84%] Linking C executable pddrive1
     1130    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE && /spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-pmpcgqf26kz
             zlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles/pd
             drive1.dir/link.txt --verbose=1
     1131    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/SRC && /spack/opt/spack
             /linux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-pmpcgqf26kzzlog
             zxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles/superl
             u_dist-static.dir/link.txt --verbose=1
     1132    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.
             4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
             7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-skylake
             /gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/includ
             e -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles
             /pddrive1.dir/pddrive1.c.o CMakeFiles/pddrive1.dir/dcreate_matrix.
             c.o -o pddrive1  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d/SRC:/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openbl
             as-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperlu_d
             ist.so.6.1.1 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0
             /openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.
             so -lm -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/par
             metis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spa
             ck/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77or
             xakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     1133    /usr/bin/ar qc libsuperlu_dist.a "CMakeFiles/superlu_dist-static.d
             ir/TreeInterface.cpp.o" "CMakeFiles/superlu_dist-static.dir/sp_ien
             v.c.o" "CMakeFiles/superlu_dist-static.dir/etree.c.o" "CMakeFiles/
             superlu_dist-static.dir/sp_colorder.c.o" "CMakeFiles/superlu_dist-
             static.dir/get_perm_c.c.o" "CMakeFiles/superlu_dist-static.dir/mmd
             .c.o" "CMakeFiles/superlu_dist-static.dir/comm.c.o" "CMakeFiles/su
             perlu_dist-static.dir/memory.c.o" "CMakeFiles/superlu_dist-static.
             dir/util.c.o" "CMakeFiles/superlu_dist-static.dir/superlu_grid.c.o
             " "CMakeFiles/superlu_dist-static.dir/pxerr_dist.c.o" "CMakeFiles/
             superlu_dist-static.dir/superlu_timer.c.o" "CMakeFiles/superlu_dis
             t-static.dir/symbfact.c.o" "CMakeFiles/superlu_dist-static.dir/psy
             mbfact.c.o" "CMakeFiles/superlu_dist-static.dir/psymbfact_util.c.o
             " "CMakeFiles/superlu_dist-static.dir/get_perm_c_parmetis.c.o" "CM
             akeFiles/superlu_dist-static.dir/mc64ad_dist.c.o" "CMakeFiles/supe
             rlu_dist-static.dir/static_schedule.c.o" "CMakeFiles/superlu_dist-
             static.dir/xerr_dist.c.o" "CMakeFiles/superlu_dist-static.dir/smac
             h_dist.c.o" "CMakeFiles/superlu_dist-static.dir/dmach_dist.c.o" "C
             MakeFiles/superlu_dist-static.dir/colamd.c.o" "CMakeFiles/superlu_
             dist-static.dir/superlu_dist_version.c.o" "CMakeFiles/superlu_dist
             -static.dir/dlangs_dist.c.o" "CMakeFiles/superlu_dist-static.dir/d
             gsequ_dist.c.o" "CMakeFiles/superlu_dist-static.dir/dlaqgs_dist.c.
             o" "CMakeFiles/superlu_dist-static.dir/dutil_dist.c.o" "CMakeFiles
             /superlu_dist-static.dir/dmemory_dist.c.o" "CMakeFiles/superlu_dis
             t-static.dir/dmyblas2_dist.c.o" "CMakeFiles/superlu_dist-static.di
             r/dsp_blas2_dist.c.o" "CMakeFiles/superlu_dist-static.dir/dsp_blas
             3_dist.c.o" "CMakeFiles/superlu_dist-static.dir/pdgssvx.c.o" "CMak
             eFiles/superlu_dist-static.dir/pdgssvx_ABglobal.c.o" "CMakeFiles/s
             uperlu_dist-static.dir/dreadhb.c.o" "CMakeFiles/superlu_dist-stati
             c.dir/dreadrb.c.o" "CMakeFiles/superlu_dist-static.dir/dreadtriple
             .c.o" "CMakeFiles/superlu_dist-static.dir/dreadtriple_noheader.c.o
             " "CMakeFiles/superlu_dist-static.dir/dbinary_io.c.o" "CMakeFiles/
             superlu_dist-static.dir/dreadMM.c.o" "CMakeFiles/superlu_dist-stat
             ic.dir/pdgsequ.c.o" "CMakeFiles/superlu_dist-static.dir/pdlaqgs.c.
             o" "CMakeFiles/superlu_dist-static.dir/dldperm_dist.c.o" "CMakeFil
             es/superlu_dist-static.dir/pdlangs.c.o" "CMakeFiles/superlu_dist-s
             tatic.dir/pdutil.c.o" "CMakeFiles/superlu_dist-static.dir/pdsymbfa
             ct_distdata.c.o" "CMakeFiles/superlu_dist-static.dir/ddistribute.c
             .o" "CMakeFiles/superlu_dist-static.dir/pddistribute.c.o" "CMakeFi
             les/superlu_dist-static.dir/pdgstrf.c.o" "CMakeFiles/superlu_dist-
             static.dir/pdgstrf2.c.o" "CMakeFiles/superlu_dist-static.dir/pdgst
             rs.c.o" "CMakeFiles/superlu_dist-static.dir/pdgstrs1.c.o" "CMakeFi
             les/superlu_dist-static.dir/pdgstrs_lsum.c.o" "CMakeFiles/superlu_
             dist-static.dir/pdgstrs_Bglobal.c.o" "CMakeFiles/superlu_dist-stat
             ic.dir/pdgsrfs.c.o" "CMakeFiles/superlu_dist-static.dir/pdgsmv.c.o
             " "CMakeFiles/superlu_dist-static.dir/pdgsrfs_ABXglobal.c.o" "CMak
             eFiles/superlu_dist-static.dir/pdgsmv_AXglobal.c.o" "CMakeFiles/su
             perlu_dist-static.dir/pdGetDiagU.c.o" "CMakeFiles/superlu_dist-sta
             tic.dir/dcomplex_dist.c.o" "CMakeFiles/superlu_dist-static.dir/zla
             ngs_dist.c.o" "CMakeFiles/superlu_dist-static.dir/zgsequ_dist.c.o"
              "CMakeFiles/superlu_dist-static.dir/zlaqgs_dist.c.o" "CMakeFiles/
             superlu_dist-static.dir/zutil_dist.c.o" "CMakeFiles/superlu_dist-s
             tatic.dir/zmemory_dist.c.o" "CMakeFiles/superlu_dist-static.dir/zm
             yblas2_dist.c.o" "CMakeFiles/superlu_dist-static.dir/zsp_blas2_dis
             t.c.o" "CMakeFiles/superlu_dist-static.dir/zsp_blas3_dist.c.o" "CM
             akeFiles/superlu_dist-static.dir/pzgssvx.c.o" "CMakeFiles/superlu_
             dist-static.dir/pzgssvx_ABglobal.c.o" "CMakeFiles/superlu_dist-sta
             tic.dir/zreadhb.c.o" "CMakeFiles/superlu_dist-static.dir/zreadrb.c
             .o" "CMakeFiles/superlu_dist-static.dir/zreadtriple.c.o" "CMakeFil
             es/superlu_dist-static.dir/zreadtriple_noheader.c.o" "CMakeFiles/s
             uperlu_dist-static.dir/zbinary_io.c.o" "CMakeFiles/superlu_dist-st
             atic.dir/zreadMM.c.o" "CMakeFiles/superlu_dist-static.dir/pzgsequ.
             c.o" "CMakeFiles/superlu_dist-static.dir/pzlaqgs.c.o" "CMakeFiles/
             superlu_dist-static.dir/zldperm_dist.c.o" "CMakeFiles/superlu_dist
             -static.dir/pzlangs.c.o" "CMakeFiles/superlu_dist-static.dir/pzuti
             l.c.o" "CMakeFiles/superlu_dist-static.dir/pzsymbfact_distdata.c.o
             " "CMakeFiles/superlu_dist-static.dir/zdistribute.c.o" "CMakeFiles
             /superlu_dist-static.dir/pzdistribute.c.o" "CMakeFiles/superlu_dis
             t-static.dir/pzgstrf.c.o" "CMakeFiles/superlu_dist-static.dir/pzgs
             trf2.c.o" "CMakeFiles/superlu_dist-static.dir/pzgstrs.c.o" "CMakeF
             iles/superlu_dist-static.dir/pzgstrs1.c.o" "CMakeFiles/superlu_dis
             t-static.dir/pzgstrs_lsum.c.o" "CMakeFiles/superlu_dist-static.dir
             /pzgstrs_Bglobal.c.o" "CMakeFiles/superlu_dist-static.dir/pzgsrfs.
             c.o" "CMakeFiles/superlu_dist-static.dir/pzgsmv.c.o" "CMakeFiles/s
             uperlu_dist-static.dir/pzgsrfs_ABXglobal.c.o" "CMakeFiles/superlu_
             dist-static.dir/pzgsmv_AXglobal.c.o" "CMakeFiles/superlu_dist-stat
             ic.dir/pzGetDiagU.c.o"
     1134    /usr/bin/ranlib libsuperlu_dist.a
  >> 1135    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0
             /openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.
             so: undefined reference to `_gfortran_concat_string'
  >> 1136    collect2: error: ld returned 1 exit status
  >> 1137    make[2]: *** [EXAMPLE/CMakeFiles/pddrive.dir/build.make:118: EXAMP
             LE/pddrive] Error 1
     1138    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
  >> 1139    make[1]: *** [CMakeFiles/Makefile2:255: EXAMPLE/CMakeFiles/pddrive
             .dir/all] Error 2
     1140    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
     1141    [ 84%] Built target superlu_dist-static
     1142    [ 84%] Linking C executable pddrive3
     1143    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE && /spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-pmpcgqf26kz
             zlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles/pd
             drive3.dir/link.txt --verbose=1
     1144    [ 84%] Linking C executable pddrive2
     1145    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.
             4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
             7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-skylake
             /gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/includ
             e -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles
             /pddrive3.dir/pddrive3.c.o CMakeFiles/pddrive3.dir/dcreate_matrix.
             c.o -o pddrive3  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d/SRC:/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openbl
             as-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperlu_d
             ist.so.6.1.1 /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0
             /openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.
             so -lm -L/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/par
             metis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spa
             ck/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77or
             xakba5dfqwrw3xh7lbb7q7gz77sg/lib -lmetis
     1146    cd /tmp/root/spack-stage/spack-stage-superlu-dist-6.1.1-k7rciudatk
             lrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/EXAMPLE && /spack/opt/s
             pack/linux-ubuntu22.04-skylake/gcc-11.2.0/cmake-3.23.2-pmpcgqf26kz
             zlogzxqhl47wva5r5pc5m/bin/cmake -E cmake_link_script CMakeFiles/pd
             drive2.dir/link.txt --verbose=1
     1147    /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openmpi-4.1.
             4-cqmipy3bjhsk5dbioidlwxm2oeyqso4b/bin/mpicc -I/spack/opt/spack/li
             nux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3xh
             7lbb7q7gz77sg/include -I/spack/opt/spack/linux-ubuntu22.04-skylake
             /gcc-11.2.0/parmetis-4.0.3-dhmpccfuw3lnjkg5x4iik7s4hi6xynrp/includ
             e -DUSE_VENDOR_BLAS  -std=c99 -O2 -g -DNDEBUG -rdynamic CMakeFiles
             /pddrive2.dir/pddrive2.c.o CMakeFiles/pddrive2.dir/dcreate_matrix.
             c.o CMakeFiles/pddrive2.dir/dcreate_matrix_perturbed.c.o -o pddriv
             e2  -Wl,-rpath,/tmp/root/spack-stage/spack-stage-superlu-dist-6.1.
             1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciud/SRC:/spack/
             opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3.20-4ur
             mse2d27wawsihuqvsax4jlr5yqgc4/lib ../SRC/libsuperlu_dist.so.6.1.1 
             /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/openblas-0.3
             .20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.so -lm -L/spa
             ck/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/parmetis-4.0.3-d
             hmpccfuw3lnjkg5x4iik7s4hi6xynrp/lib -lparmetis -L/spack/opt/spack/
             linux-ubuntu22.04-skylake/gcc-11.2.0/metis-5.1.0-77orxakba5dfqwrw3
             xh7lbb7q7gz77sg/lib -lmetis
  >> 1148    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0
             /openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.
             so: undefined reference to `_gfortran_concat_string'
  >> 1149    collect2: error: ld returned 1 exit status
  >> 1150    make[2]: *** [EXAMPLE/CMakeFiles/pddrive1.dir/build.make:118: EXAM
             PLE/pddrive1] Error 1
     1151    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
  >> 1152    make[1]: *** [CMakeFiles/Makefile2:281: EXAMPLE/CMakeFiles/pddrive
             1.dir/all] Error 2
  >> 1153    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0
             /openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.
             so: undefined reference to `_gfortran_concat_string'
  >> 1154    /usr/bin/ld: /spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0
             /openblas-0.3.20-4urmse2d27wawsihuqvsax4jlr5yqgc4/lib/libopenblas.
             so: undefined reference to `_gfortran_concat_string'
  >> 1155    collect2: error: ld returned 1 exit status
  >> 1156    make[2]: *** [EXAMPLE/CMakeFiles/pddrive3.dir/build.make:118: EXAM
             PLE/pddrive3] Error 1
     1157    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
  >> 1158    make[1]: *** [CMakeFiles/Makefile2:333: EXAMPLE/CMakeFiles/pddrive
             3.dir/all] Error 2
  >> 1159    collect2: error: ld returned 1 exit status
  >> 1160    make[2]: *** [EXAMPLE/CMakeFiles/pddrive2.dir/build.make:134: EXAM
             PLE/pddrive2] Error 1
     1161    make[2]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
  >> 1162    make[1]: *** [CMakeFiles/Makefile2:307: EXAMPLE/CMakeFiles/pddrive
             2.dir/all] Error 2
     1163    make[1]: Leaving directory '/tmp/root/spack-stage/spack-stage-supe
             rlu-dist-6.1.1-k7rciudatklrjnl2xlaxa4l3jk4b2jxa/spack-build-k7rciu
             d'
  >> 1164    make: *** [Makefile:149: all] Error 2

```

### kokkos: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package kokkos@3.0.00 --splice cmake --runner spack --replace cmake@3.23.1 --experiment kokkos --outfile /results/kokkos/3.0.00/cmake/experiment.json
```

### darshan-runtime: FAIL

Requires openmpi, won't work

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package darshan-runtime@3.0.0 --splice openmpi --runner spack --replace openmpi --experiment darshan-runtime --outfile /results/darshan-runtime/3.0.0/openmpi/experiment.json
```

### archer: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package archer@1.0.0 --splice ninja --runner spack --replace ninja --experiment archer --outfile /results/archer/1.0.0/ninja/experiment.json

tac55n53fq77yo72efcr/spack-src/llvm'

1 error found in build log:
     242    -- Performing Test CXX_SUPPORTS_FFUNCTION_SECTIONS - Success
     243    -- Performing Test C_SUPPORTS_FDATA_SECTIONS
     244    -- Performing Test C_SUPPORTS_FDATA_SECTIONS - Success
     245    -- Performing Test CXX_SUPPORTS_FDATA_SECTIONS
     246    -- Performing Test CXX_SUPPORTS_FDATA_SECTIONS - Success
     247    -- Found PythonInterp: /spack/opt/spack/linux-ubuntu22.04-skylake/g
            cc-11.2.0/python-3.9.13-a7owmregm4a2ef43uk4x6eyjngeqymej/bin/python
            3.9
  >> 248    CMake Error at CMakeLists.txt:618 (if):
     249      if given arguments:
     250    
     251        "VERSION_LESS" "2.7"
     252    
     253      Unknown arguments specified
     254    
```

### petsc: FAIL

Won't work, requires openmpi.

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package petsc@3.10.0 --splice openmpi --runner spack --replace openmpi --experiment petsc --outfile /results/petsc/3.10.0/openmpi/experiment.json
```

### qthreads: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package qthreads@1.10 --splice hwloc --runner spack --replace hwloc --experiment qthreads --outfile /results/qthreads/1.10/hwloc/experiment.json
```

### swig: SUCCESS

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package swig@1.3.40 --splice pkgconf --runner spack --replace pkgconf@1.8.0 --experiment swig --outfile /results/swig/1.3.40/pkgconf/experiment.json
```

### pumi: FAIL

Won't work, requires openmpi.

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package pumi@2.1.0 --splice openmpi --runner spack --replace openmpi --experiment pumi --outfile /results/pumi/2.1.0/openmpi/experiment.json
```

### sundials: FAIL

Won't work, requires openmpi.

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package sundials@2.6.2 --splice openmpi --runner spack --replace openmpi --experiment sundials --outfile /results/sundials/2.6.2/openmpi/experiment.json
```

### tasmanian: FAIL

```bash
docker run -v /home/vanessa/Desktop/Code/spliced-experiment/cache:/cache -v /home/vanessa/Desktop/Code/spliced-experiment/spack-opt:/spack/opt -v /home/vanessa/Desktop/Code/spliced-experiment/results:/results -it ghcr.io/buildsi/spliced-experiment:latest spack python /code/scripts/run_spliced.py splice --package tasmanian@5.0 --splice cmake --runner spack --replace cmake --experiment tasmanian --outfile /results/tasmanian/5.0/cmake/experiment.json

==> [2022-07-29-02:34:00.028614, 12] 12: tasmanian: Executing phase: 'install'
==> [2022-07-29-02:34:00.158737, 12] WRITE LOCK (spack-stage-tasmanian-5.0-mhfh4z733pzipglyd6ylht7g3tj65lra): /tmp/root/spack-stage/.lock[4614188461280527411:1] [Released at 02:34:00.158697] 
==> [2022-07-29-02:34:00.185550, 1] Error: OSError: No such file or directory: '/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.2.0/tasmanian-5.0-mhfh4z733pzipglyd6ylht7g3tj65lra/share/Tasmanian/testing'

/spack/var/spack/repos/builtin/packages/tasmanian/package.py:180, in setup_smoke_test:
        177            tty.msg('Error tasmanian test: CMake 3.10 or higher is required')
        178            return
        179
  >>    180        install_tree(self.prefix.share.Tasmanian.testing,
        181                     join_path(self.install_test_root, 'testing'))
        182        self.cmake_bin(set=True)

See build log for details:
```
