#!/usr/bin/env python3

# This is a small script to let you easily test cle over a set of binares / .so libraries
# In this case we are using those in a spack install. You can change the root location below.

import traceback
import pickle
import fnmatch
import os
import sys
import cle

# Change this to be your spack install
root = "/p/vast1/build/spack/opt/spack"


def recursive_find(base, pattern="*.so"):
    """
    Find all .so (or other pattern of files) below a root
    """
    for root, _, filenames in os.walk(base):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)


if os.path.exists("working-libs.pkl"):
    with open("working-libs.pkl", "rb") as fd:
        working = pickle.load(fd)
else:
    working = set()


def get_basename(filename):
    return os.path.basename(filename).split(".")[0].split("-")[0]


skips = {
    "/tmp/spack/opt/spack/linux-debian11-skylake/gcc-12.1.0/libbsd-0.11.5-ayxy3zjyufi6neh4fl5pie6n6rdc3jyn/lib/libbsd.so",
    "/tmp/spack/opt/spack/linux-debian11-skylake/gcc-12.1.0/warpx-22.06-yimecrpkms6r44o7qegvo33qaejos7vx/lib/libwarpx.3d.so"  # memory killed
    "/p/vast1/build/spack/opt/spack/linux-rhel7-broadwell/gcc-10.2.1/cuda-11.5.1-qmldae2ji6fe3pjaau3ubcmnor2fc2lm/nvvm/lib64/libnvvm.so",  # too long
    "libtbb.so",
    "LLVMgold.so",
    "libclang.so",
    "liblldb.so",  # out of memory
}

new_skips = set()
for skip in skips:
    new_skips.add(get_basename(skip))
skips = skips.union(new_skips)

for filename in recursive_find(root):

    # Intel ones don't seem to work:
    if (
        "intel" in filename
        or "hpctoolkit/ext-libs" in filename
        or "librustc_driver" in filename
    ):
        print(f"Skipping {filename}")
        continue

    # Also check the basename in case duplicate names
    basename = get_basename(filename)

    if filename in working or basename in working:
        print(f"Skipping {filename} as working.")
        continue
    if filename in skips or basename in skips:
        print(f"Skipping {filename} as skip.")
        continue
    try:
        print(f"Testing {filename}...")
        ld = cle.Loader(filename, load_debug_info=True, auto_load_libs=False)
        working.add(filename)
        working.add(basename)

        # Always update working
        with open("working-libs.pkl", "wb") as o:
            pickle.dump(working, o)

    except Exception as e:
        print(traceback.format_exc())
        print(f"{filename} is not working: {e}")
        sys.exit()

print(f"{len(working)} libraries are parse-able, yay!")
