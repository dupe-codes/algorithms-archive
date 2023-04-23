#!/usr/bin/env python3

"""
Command line utility to zip and unzip files using Huffman coding algorithm [1].

[1] https://en.wikipedia.org/wiki/Huffman_coding
"""

import argparse

from encoder import HuffmanEncoder


def parse_args() -> argparse.Namespace:
    """ Parses the command line arguments """
    parser = argparse.ArgumentParser(
        description='Zip and unzip files using Huffman coding.')
    parser.add_argument('input_path', help='path to the input file')
    parser.add_argument('output_path', help='path to the desired output file')
    parser.add_argument('-d', '--decode', action='store_true',
                        help='decode the input file')
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    encoder = HuffmanEncoder()
    if args.decode:
        encoder.decode(args.input_path, args.output_path)
    else:
        encoder.encode(args.input_path, args.output_path)


if __name__ == '__main__':
    main()
