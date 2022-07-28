FROM ghcr.io/buildsi/libabigail:2.0

# docker build -t ghcr.io/buildsi/spliced-experiment .
# docker run -it -v /p/vast1/build/spliced-cache:/cache /p/vast1/build/spack:/spack ghcr.io/buildsi/spliced-experiment

ENV CMAKE_VERSION=3.20.4
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y build-essential gfortran patchelf

# always build with debug (this is in template script too)
ENV SPACK_ADD_DEBUG_FLAGS=true
ENV SPACK_DISABLE_LOCAL_CONFIG=true
ENV SPACK_USER_CACHE_PATH=/cache/spack
   
# Always save to this cache (should be bound from the host)
ENV SPLICED_SMEAGLE_CACHE_DIR=/cache
ENV SPLICED_ABILAB_CACHE_DIR=/cache

# Assume spack bound to /spack
ENV PATH=/spack/bin:$PATH

# Install cle (dependency of spliced)
RUN git clone https://github.com/vsoch/cle && \
    cd cle && \

    # archinfo, pyvex, pyelftools, then cle
    pip install wheel && \
    pip install git+https://github.com/angr/archinfo && \
    pip install git+https://github.com/angr/pyvex && \
    pip install git+https://github.com/eliben/pyelftools && \
    pip install .

RUN pip install git+https://github.com/buildsi/spliced@main

# Install abi-laboratory tools
RUN git clone https://github.com/lvc/abi-dumper && \
    cd abi-dumper && \
    make install prefix=/usr && \
    cd .. && \
    git clone https://github.com/lvc/abi-compliance-checker && \
    cd abi-compliance-checker && \
    make install prefix=/usr

# Install "nice to haves" and try to provide cmake
RUN pip install ipython && apt-get install -y vim && \
    curl -s -L https://github.com/Kitware/CMake/releases/download/v$CMAKE_VERSION/cmake-$CMAKE_VERSION-linux-x86_64.sh > cmake.sh && \
    sh cmake.sh --prefix=/usr/local --skip-license && \
    rm cmake.sh

# Try installing spack to inside of container (and will bind install on outside)
# Don't install modules, and change var cache path
RUN git clone --depth 1 -b vsoch/db-17-splice-july-25 https://github.com/vsoch/spack /spack && \
    spack config add 'modules:default:enable::[]' && \
    spack config add config:source_cache:/cache/spack-cache && \
    /spack/bin/spack compiler find && \
    mkdir -p /results

# Add scripts
WORKDIR /code
COPY . /code
