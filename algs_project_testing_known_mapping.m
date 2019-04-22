flickr_lastfm = load('flickr-lastfm.mat');
flickr = flickr_lastfm.flickr; 
flickr_node_label = flickr_lastfm.flickr_node_label; 
flickr_edge_label = flickr_lastfm.flickr_edge_label; 
lastfm = flickr_lastfm.lastfm; 
lastfm_node_label = flickr_lastfm.lastfm_node_label; 
lastfm_edge_label = flickr_lastfm.lastfm_edge_label; 
alpha = flickr_lastfm.alpha; 
H = flickr_lastfm.H; 
maxiter = flickr_lastfm.maxiter; 
tol = flickr_lastfm.tol; 
gndtruth = flickr_lastfm.gndtruth; 

%% run flickr-lastfm
alpha = 0.3; maxiter = 30; tol = 1e-4;
S = FINAL(flickr, lastfm, flickr_node_label, lastfm_node_label, flickr_edge_label, lastfm_edge_label, H, alpha, maxiter, tol);
    
M = greedy_match(S);
[row, col] = find(M);
acc = size(intersect([col row], gndtruth, 'rows'), 1)/size(gndtruth, 1);


douban = load('Douban.mat');
offline = douban.offline; 
offline_node_label = douban.offline_node_label; 
offline_edge_label = douban.offline_edge_label; 
online = douban.online; 
online_node_label = douban.online_node_label; 
online_edge_label = douban.online_edge_label; 
H = douban.H; 
ground_truth = douban.ground_truth; 

%% run douban
alpha = 0.82; maxiter = 30; tol = 1e-4;
S = FINAL(online, offline, online_node_label, offline_node_label, online_edge_label, offline_edge_label, H, alpha, maxiter, tol);

M = greedy_match(S);
[row, col] = find(M);
acc = size(intersect([col row], ground_truth, 'rows'), 1)/size(ground_truth, 1);   
