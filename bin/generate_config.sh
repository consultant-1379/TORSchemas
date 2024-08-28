#!/bin/bash

BDIR=$(dirname $(cd $(dirname $0) ; pwd))

cd ${BDIR}/python/solution_set
for file in $(ls *.py | grep -v __init__) ; do
    PF=$(echo $file | sed 's/\.py$//')
    CN=$(awk '$1 ~ /^class$/ { gsub(/\(.*/, "", $2) ; print $2 }' ${file})
    echo "${PF}=solution_set.${PF}.${CN}"
done
