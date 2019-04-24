import argparse
import numpy as np
import random


def parse_args():
    parser = argparse.ArgumentParser(description='Create H matrix based on node degree similarity')
    parser.add_argument('-i1', '--input_file1', default=None, help='Enter the file path to the input file 1.')
    parser.add_argument('-i2', '--input_file2', default=None, help='Enter the file path to the input file 2.')
    parser.add_argument('-g', '--ground_truth', default=None, help='Ground truth.')
    parser.add_argument('-o', '--output_file', default=None, help='Enter the file path to output file.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    random.seed(42)

    edge_matrix1 = np.loadtxt(args.input_file1, delimiter=',', dtype=np.int)
    edge_matrix2 = np.loadtxt(args.input_file2, delimiter=',', dtype=np.int)

    ground_truth = np.loadtxt(args.ground_truth, delimiter=',', dtype=np.int)

    n1 = len(edge_matrix1)
    n2 = len(edge_matrix2)

    degree1 = np.sum(edge_matrix1, 0)
    degree2 = np.sum(edge_matrix2, 0)

    H = np.zeros(shape=(n2, n1))

    n1_max = np.max(degree1)

    for i in range(len(edge_matrix2)):
        H[i, :] = abs(degree1 - degree2[i]) / max(degree2[i], n1_max)

    idx = np.asarray(random.sample(
        list(np.linspace(0, (n2 * n1) - 1, n2 * n1)), round(0.9996 * (n2 * n1) - 1))).astype('int')

    H_temp = np.copy(H)
    H = H / np.sum(H)

    H = H.ravel()
    H[idx] = 0
    H = np.reshape(H, (n2, n1))

    if args.ground_truth is not None:
        H[ground_truth[:, 1] - 1, ground_truth[:, 0] - 1] = H_temp[ground_truth[:, 1] - 1, ground_truth[:, 0] - 1]

    if args.output_file is None:
        args.output_file = './H.csv'

    np.savetxt(args.output_file, H, delimiter=',', fmt='%f')
