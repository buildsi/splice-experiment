# Error Summary

I'm going to attempt to capture errors I see and summarize. Logs are in `logs`
in the experiments space, and I'll move them into `logs/seen` after I've seen.
The jobs are running slowly enough to make this possible. If something appears in
the listing below, it has something nasty in the error log. If I don't see obvious
error I'll increment the counter below. Haven't you heard of Markdown programming?

 - completed no obvious error count: 8
 - I accidentally moved and they weren't done yet: 3


## Valid Errors

These are errors that I deem to be valid in the sense it's not a weird spack lock
error. It's simply a build that failed likely because of ABI or similar.

```bash
r unexpected token `HWLOC,hwloc'
```

- aml-master-numactl-experiment.err

```bash
Extension error
Could not import extension breathe (exception: No module named 'bre
            athe')
```
- aml-0.1.0-numactl-experiment.err


```bash
nfo.so.6: error adding symbols: DSO missing from command line
```

- arborx-1.0-cmake-experiment.err 

```bash
 /libtinfo.so.6: error adding symbols: DSO missing from command lin
```

- arborx-1.1-cmake-experiment.err
- bolt-2.0-cmake-experiment.err 

```bash
 undefined reference to symbol 'cbreak@@@@NCURSES6_TINFO_5.0.19991023
```
- arborx-master-cmake-experiment.err

```bash
error: no member named 'ArgumentListType'
```
- archer-1.0.0-ninja-experiment.err

```bash
error: argument is incompatible with formal parameter
```
- archer-2.0.0-llvm-experiment.err
- archer-2.0.0-llvm-openmp-ompt-experiment.err 

```
No such file or directory: 't/wrap/aclocal.in'
```
-  bolt-1.0-automake-experiment.err 
-  bolt-1.0.1-automake-experiment.err
-  bolt-2.0-automake-experiment.err 
-  bolt-main-automake-experiment.err 

## Action Errors

These are errors we might want to do something about.

```bash
AssertionError exception when releasing read lock 
```
This looks like it might be the lock error we saw - it only showed up when (at least that I'm aware of) more jobs wre running.

- archer-1.0.0-cmake-experiment.err
- archer-1.0.0-llvm-experiment.err
- archer-1.0.0-llvm-openmp-ompt-experiment.err 
- bolt-1.0-cmake-experiment.err
- bolt-1.0.1-cmake-experiment.err
- bolt-main-cmake-experiment.err

```bash
Error: Failed to install adiak due to LockTimeoutError: Timed out waiting for a write lock.
```

- caliper-1.7.0-adiak-experiment.err

```bash
<blank>
```

The above is purposefully blank - I'm seeing jobs with no output and error logs. I'm wondering if this is still the lock error.

- archer-2.0.0-ninja-experiment.err

```bash
error: *** JOB 2580812 ON borax29 CANCELLED AT 2022-04-04T09:15:48 DUE TO TIME LIMIT ***
```
This job has very little output and just the cancelled, maybe it's still the lock issue?

- archer-2.0.0-cmake-experiment.err

```bash
If you are willing to be a maintainer for this version of the package, submit a PR to remove `deprecated=False`, or use `--deprecated` to skip this check.
```

This error basically says we need to add the `--deprecated` flag.

- arborx-0.9-beta-cmake-experiment.err 
- arborx-0.9-beta-kokkos-experiment.err
- arborx-0.9-beta-openmpi-experiment.err
- arborx-1.0-openmpi-experiment.err
- arborx-1.1-openmpi-experiment.err
- bolt-1.0-libtool-experiment.err
- bolt-1.0.1-libtool-experiment.err
- bolt-2.0-libtool-experiment.err 
- bolt-main-libtool-experiment.err 

```bash
fatal: Remote branch master not found in upstream origin
==> Warning: Spack was unable to fetch url list due to a certificate verification problem. You can try running spack -k, which will not check SSL certificates. Use this at your own risk
```
This we might be able to fix by either catching and then checking any error for the word "cerificate" and trying again with `-k` - I'd be cautious about just applying it globally.

- arborx-master-openmpi-experiment.err
