import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description='Generate ground truth for the network.')
    parser.add_argument('input_file', default=None, help='Enter the file path to the input file.')
    parser.add_argument('-o', '--output_file', default=None, help='Enter the file path to output file.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    edge_matrix = np.loadtxt(args.input_file, delimiter=',', dtype=np.int)

    edge_list = []

    for i in range(len(edge_matrix)):
        for j in range(len(edge_matrix)):
            if edge_matrix[i, j] == 1:
                edge_list.append([i + 1, j + 1])

    if args.output_file is None:
        args.output_file = './edge_list.csv'

    np.savetxt(args.output_file, edge_list, delimiter=',', fmt='%i')
