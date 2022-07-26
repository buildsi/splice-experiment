#!/bin/bash

# This script will be called by the abi-laboratory runner.

old=$1
new=$2
name=${3:-NAME}
report_path="${4}"
cleanup=false

printf "old: $old\n"
printf "new: $new\n"
printf "report: $report_path\n"


# cleanup if no custom report path is provided
if [ -z "${report_path+xxx}" ]; then 
    report_path=$(mktemp /tmp/report-XXXXX.html);
    printf "No report path provided, setting to $report_path\n"
    cleanup=true
fi
if [ -z "${old+xxx}" ]; then echo "Missing first argument, old library"; exit 1; fi
if [ -z "${new+xxx}" ]; then echo "Missing second argument, new library"; exit 1; fi

dump_old=$(mktemp /tmp/ABI-1-XXXXX.dump)
dump_new=$(mktemp /tmp/ABI-2-XXXXX.dump)

# Options: https://github.com/lvc/abi-dumper/blob/master/abi-dumper.pl#L112
abi-dumper $old -o $dump_old -lver 1
abi-dumper $new -o $dump_new -lver 2

# Options: https://github.com/lvc/abi-compliance-checker/blob/master/abi-compliance-checker.pl#L119
abi-compliance-checker -l $name -old $dump_old -new $dump_new -report-path $report_path
rm $dump_old
rm $dump_new

if [[ "${cleanup}" == "true" ]]; then
    rm $report_path
fi
