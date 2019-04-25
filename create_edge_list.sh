#!/bin/bash

# Note, spaces in the double quotes here breaks it. thanks matlab.
for filename in ../yeast_rw/*.csv; do
    file=$(basename "$filename")
    python3 ./network_processing/edge_matrix_to_list.py $filename -o ../yeast_rw_edge_list/$file
done
