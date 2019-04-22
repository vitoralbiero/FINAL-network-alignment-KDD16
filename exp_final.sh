#!/bin/bash

N1="../krogan_2007_adj_mat.csv"
N2="../yeast+5rw_0.csv"
GRN="../krogan_ground_truth.txt"

# Note, spaces in the double quotes here breaks it. thanks matlab.
matlab -nodesktop -nosplash -nodisplay -nojvm -r "known_mapping_test('$N1','$N2','$GRN');exit;" 
