#!/bin/bash

N1="../krogan_2007_adj_mat_random.csv"
GRN="../krogan_2007_adj_mat_random_ground_truth.csv"

# Note, spaces in the double quotes here breaks it. thanks matlab.
for filename in ../yeast_rw/*.csv; do
    H_path="../yeast_rw_H_mod/H_krogan_2007_$(basename $filename)"
    matlab -nodesktop -nosplash -nodisplay -nojvm -r "known_mapping_test('$N1','$filename','$GRN','$H_path');exit;"
done
