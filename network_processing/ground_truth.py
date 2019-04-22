import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description='Convert the LEDA graph representation into an adj matrix.')
    parser.add_argument('input_file', default=None, help='Enter the file path to the input file.')
    parser.add_argument('-o', '--output_file', default=None, help='Enter the file path to output file.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    edge_matrix = np.loadtxt(args.input_file, delimiter=' ', dtype=np.str)

    idx = np.linspace(1, len(edge_matrix), len(edge_matrix))
    ground_truth = np.transpose(np.array([idx, idx]))
    print(ground_truth.shape)

    if args.output_file is None:
        args.output_file = './ground_truth.csv'

    np.savetxt(args.output_file, ground_truth, delimiter=' ', fmt='%i')
