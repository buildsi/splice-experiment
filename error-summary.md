# Error Summary

I'm going to attempt to capture errors I see and summarize. Logs are in `logs`
in the experiments space, and I'll move them into `logs/seen` after I've seen.
The jobs are running slowly enough to make this possible. If something appears in
the listing below, it has something nasty in the error log. If I don't see obvious
error I'll increment the counter below. Haven't you heard of Markdown programming?

 - completed no obvious error count: 3

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


```bash
 undefined reference to symbol 'cbreak@@@@NCURSES6_TINFO_5.0.19991023
```
- arborx-master-cmake-experiment.err

## Action Errors

These are errors we might want to do something about.

```bash
If you are willing to be a maintainer for this version of the package, submit a PR to remove `deprecated=False`, or use `--deprecated` to skip this check.
```

This error basically says we need to add the `--deprecated` flag.

- arborx-0.9-beta-cmake-experiment.err 
- arborx-0.9-beta-kokkos-experiment.err

```bash
fatal: Remote branch master not found in upstream origin
==> Warning: Spack was unable to fetch url list due to a certificate verification problem. You can try running spack -k, which will not check SSL certificates. Use this at your own risk
```
This we might be able to fix by either catching and then checking any error for the word "cerificate" and trying again with `-k` - I'd be cautious about just applying it globally.

- arborx-master-openmpi-experiment.err
