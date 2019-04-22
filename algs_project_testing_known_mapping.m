krogan = readtable('krogan_2007_adj_mat.csv');
krogan_node_label =[];
krogan_edge_label = {};

noisy = readtable('yeast+5rw_0.csv');
noisy_node_label = []; 
noisy_edge_label = {}; 

%% Uniform similarity matrix.
H = ones(size(noisy)[0], size(krogan)[0]) / (size(noisy)[0] + size(krogan)[0])

%% run krogan-noisy
alpha = 0.3; maxiter = 30; tol = 1e-4;
S = FINAL(krogan, noisy, krogan_node_label, noisy_node_label, krogan_edge_label, noisy_edge_label, H, alpha, maxiter, tol);

%% Saves the matrix:
csvwrite('krogan_vs_yeast+5rw_0.csv', S)
    
M = greedy_match(S);
[row, col] = find(M);
acc = size(intersect([col row], gndtruth, 'rows'), 1)/size(gndtruth, 1);