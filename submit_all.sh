#!/bin/bash

for experiment in $(find ./splices -name experiment.yaml); do
    python submit_jobs.py $experiment results
done
