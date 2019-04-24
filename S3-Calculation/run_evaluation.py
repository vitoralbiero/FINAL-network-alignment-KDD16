import Evaluation
import os

true_mapping_name = None
goterm_name1 = None
goterm_name2 = None

eval_NC_P = True
eval_NC_R = True
eval_NC_F = True
eval_GS3 = True
eval_NCV = False
eval_NCV_GS3 = False
eval_GC = False
eval_PF_P = False
eval_PF_R = False
eval_PF_F = False

network_dir = "../../test_nets/"
num = 0
results = {}
graph1 = "../../krogan_2007_adj_list_random.gw"
# mapping_name = "../../krogan_2007_adj_mat_random_vs_yeast+10rw_0_alignment.aln"
mapping_name = "../../krogan_2007_adj_mat_random_vs_yeast+10rw_1_alignment.csv"
f = open("results.csv", "w+")
for file in os.listdir(network_dir):
    if file.endswith(".gw"):
        graph2 = os.path.join(network_dir, file)
        # mapping_name =
        quality = Evaluation.AlignmentQuality(graph1, graph2, mapping_name,
                                              true_mapping_name, goterm_name1, goterm_name2)
        score = quality.evaluate(eval_NC_P, eval_NC_R, eval_NC_F, eval_GS3, eval_NCV,
                                 eval_NCV_GS3, eval_GC, eval_PF_P, eval_PF_R, eval_PF_F)
        print(score)
        results[file] = score
        f.write(file + "," + str(score["GS3"]) + "\n")
        num = num + 1
print num
print results
