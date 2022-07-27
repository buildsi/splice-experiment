## Plan

Here is the plan! 

### Matrix Automated Tests

We will first need to choose a set of compilers appropriate for a scoped analysis (likely related to what Smeagle can parse). The [manual/experiments/e4s.yaml](manual/experiments/e4s.yaml) will be run with a custom Python script
that reads in each e4s package, and:

```bash
For every package in e4s K with tests:
  For every dependency of package K, D that is also in e4s:
    Perform splice of package K and dependency D
       Provide splice metadata to predictor P to get a prediction.
```

The spack tests repesent our best effort for a ground truth, as a developer that writes
test is making (we hope) a best effort to test functionality. Minimally the spack-test
predictor invokes the actual loader, which would catch basic symbols issues, etc.

This means that we also need to know the sample of the e4s packages that have tests.
I wrote a script to do that. See the [manual](manual) directory for more.


