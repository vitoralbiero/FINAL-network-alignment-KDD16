#!/bin/bash

# Note, spaces in the double quotes here breaks it. thanks matlab.
for filename in ../yeast_rw_edge_list/*.csv; do
    file=$(basename "$filename")
    python3 ./network_processing/list2leda.py $filename
done
