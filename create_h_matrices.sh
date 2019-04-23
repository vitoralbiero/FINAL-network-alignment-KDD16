#!/bin/bash

N1="../krogan_2007_adj_mat_random.csv"
GRN="../krogan_2007_random_ground_truth.csv"

# Note, spaces in the double quotes here breaks it. thanks matlab.
for filename in ../yeast_rw/*.csv; do
    file=$(basename "$filename")
    python3 ./network_processing/H_matrix.py -i1 $N1 -i2 $filename -g $GRN -o ../yeast_rw_H/H_krogan_2007_$file
done
