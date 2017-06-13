#!/bin/bash
set -e
set -u

mkdir -p results

for file in *.fasta
do 
echo "found $file"
mafft --auto $file > results/"${file}"_output.txt
echo "completed Multiple Alignment on $file"
done
