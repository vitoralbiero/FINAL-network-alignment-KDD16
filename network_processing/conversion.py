import argparse
import csv

import numpy as np
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description='Convert the LEDA graph representation into an adj matrix.')
    parser.add_argument('input_file', default=None, help='Enter the file path to the input file.')
    parser.add_argument('-o', '--output_file', default=None, help='Enter the file path to output file.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    with open(args.input_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=' ')

        # ignore these lines.
        for junk in range(4):
            print(next(csv_reader))

        node_count = int(next(csv_reader)[0])

        # Create empty adjacency list.
        adj_mat = np.zeros((node_count, node_count))

        ignore_node_ids = True
        for row in csv_reader:
            if ignore_node_ids and row[0][0] == '|':
                continue
            elif ignore_node_ids and row[0][0] != '|':
                ignore_node_ids = False
                print(row)
            else:  # save the edge adj. list
                # convert nodes from 1 index to 0 index & save edge presence
                adj_mat[int(row[0]) - 1, int(row[1]) - 1] = 1

        if args.output_file is None:
            args.output_file = './adj_mat.csv'

        df = pd.DataFrame(adj_mat, dtype=int)
        df.to_csv(args.output_file, header=None, index=False)
