import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description='Generate ground truth for the network.')
    parser.add_argument('input_file', default=None, help='Enter the file path to the input file.')
    parser.add_argument('-o', '--output_file', default=None, help='Enter the file path to output file.')

    return parser.parse_args()


if __name__ == '__main__':
    np.random.seed(42)
    args = parse_args()

    edge_matrix = np.loadtxt(args.input_file, delimiter=',', dtype=np.int)

    idx1 = np.linspace(0, len(edge_matrix) - 1, len(edge_matrix)).astype('int')

    idx2 = np.linspace(0, len(edge_matrix) - 1, len(edge_matrix)).astype('int')
    np.random.shuffle(idx2)

    edge_matrix_flipped = np.copy(edge_matrix)
    edge_matrix_flipped = edge_matrix[idx2, :][:, idx2]

    ground_truth = np.transpose(np.array([idx1 + 1, idx2 + 1]))

    if args.output_file is None:
        args.output_file = './ground_truth.csv'

    np.savetxt(args.output_file, ground_truth, delimiter=',', fmt='%i')
    np.savetxt(args.input_file[:-4] + '_random.csv', edge_matrix_flipped, delimiter=',', fmt='%i')
