function unknown_mapping_test(netpath1, netpath2)

net1 = table2array(readtable(netpath1));
net1_node_label = [];
net1_edge_label = {};

net2 = table2array(readtable(netpath2));
net2_node_label = []; 
net2_edge_label = {}; 

%% H matrix with uniform distribution
H = ones(size(net2, 1), size(net1, 1)) / (size(net2, 1) * size(net1, 1));

%% run net1 vs net2
alpha = 0.3; maxiter = 30; tol = 1e-4;
S = FINAL(net1, net2, net1_node_label, net2_node_label, net1_edge_label, net2_edge_label, H, alpha, maxiter, tol);

%% Saves the matrix:
netpath1_substr = strsplit(netpath1, '.');
netpath1_substr = netpath1_substr{size(netpath1_substr,2)-1};
netpath1_substr = strsplit(netpath1, '/');
netpath1_substr = netpath1_substr{size(netpath1_substr,2)};

netpath2_substr = strsplit(netpath2, '.');
netpath2_substr = netpath2_substr{size(netpath2_substr,2)-1};
netpath2_substr = strsplit(netpath2, '/');
netpath2_substr = netpath2_substr{size(netpath2_substr,2)};

csvwrite(strcat('../unknown_mapping_output/', netpath1_substr(1:length(netpath1_substr)-4),...
                '_vs_', netpath2_substr(1:length(netpath2_substr)-4), '.csv'), S);

M = greedy_match(S);
[row, col] = find(M);

%% Saves prediction (alignment)
csvwrite(strcat('../unknown_mapping_output/', netpath1_substr(1:length(netpath1_substr)-4),...
                '_vs_', netpath2_substr(1:length(netpath2_substr)-4), '_alignment.csv'), [row, col]);

exit;
