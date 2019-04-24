import Evaluation
import os

true_mapping_name = None
goterm_name1 = None
goterm_name2 = None

eval_NC_P = False
eval_NC_R = False
eval_NC_F = False
eval_GS3 = True
eval_NCV = False
eval_NCV_GS3 = False
eval_GC = False
eval_PF_P = False
eval_PF_R = False
eval_PF_F = False

network_dir = "/home/aidan/ND/Algs/Project/test_nets/"
num = 0
results = {}
graph1 = "/home/aidan/ND/Algs/Project/krogan_2007_adj_list_random.gw"
mapping_name = "/home/aidan/ND/Algs/Project/krogan_2007_adj_mat_random_vs_yeast+10rw_0_alignment.aln"
f = open("results.csv", "w+")
for file in os.listdir(network_dir):
    if file.endswith(".gw"):
	graph2 = os.path.join(network_dir, file)
	#mapping_name = 
	quality = Evaluation.AlignmentQuality(graph1, graph2, mapping_name, true_mapping_name, goterm_name1, goterm_name2);
	score = quality.evaluate(eval_NC_P, eval_NC_R, eval_NC_F, eval_GS3, eval_NCV, eval_NCV_GS3, eval_GC, eval_PF_P, eval_PF_R, eval_PF_F)
	results[file] = score
	f.write(file + "," + str(score["GS3"]) + "\n")
	num = num + 1
print num
print results
