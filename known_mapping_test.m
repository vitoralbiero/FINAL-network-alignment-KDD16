function known_mapping_test(netpath1, netpath2, ground_truth_path, H_path)

net1 = table2array(readtable(netpath1));
net1_node_label = [];
net1_edge_label = {};

noisy = table2array(readtable(netpath2));
noisy_node_label = []; 
noisy_edge_label = {}; 

%% H matrix based on prior knowledge (node similarity + ground truth)
H = table2array(readtable(H_path));

%% run net1 vs noisy
alpha = 0.3; maxiter = 30; tol = 1e-4;
S = FINAL(net1, noisy, net1_node_label, noisy_node_label, net1_edge_label, noisy_edge_label, H, alpha, maxiter, tol);

%% Saves the matrix:
netpath1_substr = strsplit(netpath1, '.');
netpath1_substr = netpath1_substr{size(netpath1_substr,2)-1};
netpath1_substr = strsplit(netpath1, '/');
netpath1_substr = netpath1_substr{size(netpath1_substr,2)};

netpath2_substr = strsplit(netpath2, '.');
netpath2_substr = netpath2_substr{size(netpath2_substr,2)-1};
netpath2_substr = strsplit(netpath2, '/');
netpath2_substr = netpath2_substr{size(netpath2_substr,2)};

csvwrite(strcat('../known_mapping_output/', netpath1_substr(1:length(netpath1_substr)-4),...
                '_vs_', netpath2_substr(1:length(netpath2_substr)-4), '.csv'), S);

%% Check ground truth accuracy
ground_truth = table2array(readtable(ground_truth_path));
M = greedy_match(S);
[row, col] = find(M);

acc = size(intersect([col row], ground_truth, 'rows'), 1)/size(ground_truth, 1)

%% Saves prediction (alignment) and accuracy
csvwrite(strcat('../known_mapping_output/', netpath1_substr(1:length(netpath1_substr)-4),...
                '_vs_', netpath2_substr(1:length(netpath2_substr)-4), '_alignment.csv'), [row, col]);
csvwrite(strcat('../known_mapping_output/', netpath1_substr(1:length(netpath1_substr)-4),...
                '_vs_', netpath2_substr(1:length(netpath2_substr)-4), '_acc.csv'), acc);

exit;
