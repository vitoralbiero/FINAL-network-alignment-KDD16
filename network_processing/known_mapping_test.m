function known_mapping_test(netpath1, netpath2, ground_truth_path)

net1 = table2array(readtable(netpath1));
net1_node_label =[];
net1_edge_label = {};

noisy = table2array(readtable(netpath2));
noisy_node_label = []; 
noisy_edge_label = {}; 

%% Uniform similarity matrix.
H = ones(size(noisy, 1), size(net1, 1)) / (size(noisy, 1) + size(net1, 1))

%% run net1 vs noisy
alpha = 0.3; maxiter = 30; tol = 1e-4;
S = FINAL(net1, noisy, net1_node_label, noisy_node_label, net1_edge_label, noisy_edge_label, H, alpha, maxiter, tol);

%% Saves the matrix:
netpath1_substr = strsplit(netpath1, '.')
netpath1_substr = netpath1_substr{size(netpath1_substr,2)-1}

netpath2_substr = strsplit(netpath2, '.')
netpath2_substr = netpath2_substr{size(netpath2_substr,2)-1}

csvwrite(strcat(netpath1_substr, '_vs_', netpath2_substr, '.csv'), S);

%% Check ground truth accuracy
ground_truth = table2array(readtable(ground_truth_path));
M = greedy_match(S);
[row, col] = find(M);
acc = size(intersect([col row], ground_truth, 'rows'), 1)/size(ground_truth, 1)

exit;
