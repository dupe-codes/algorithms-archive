"""
Command line utility for zip and unzip files using Huffman coding.
"""

import argparse

from huffman_encoder.encoder import HuffmanEncoder

def parse_args() -> argparse.Namespace:
    """ Parses the command line arguments """
    parser = argparse.ArgumentParser(description='Zip and unzip files using Huffman coding.')
    parser.add_argument('input_path', help='path to the input file')
    parser.add_argument('output_path', help='path to the output file')
    parser.add_argument('-d', '--decode', action='store_true', help='decode the input file')
    return parser.parse_args()

def decode(input_path: str, output_path: str) -> None: 
    """ Decodes the input file and writes the output to the output file """
    encoder = HuffmanEncoder()

    with open(input_path, 'r') as input_file:
        input_lines = input_file.readlines()
        encoder.fit_decoder(input_lines)
        decoded = encoder.decode(input_lines)
     
    with open(output_path, 'w') as output_file:
        output_file.writelines(decoded)

def encode(input_path: str, output_path: str) -> None:
    """ Encodes the input file and writes the output to the output file """
    encoder = HuffmanEncoder()
    with open(input_path, 'r') as input_file:
        input_lines = input_file.readlines()
        encoder.fit_encoder(input_lines)
        encoded = encoder.encode(input_lines)

    with open(output_path, 'w') as output_file:
        output_file.writelines(encoder.encode(encoded))

def main() -> None:
    args = parse_args()

    if args.decode:
        decode(args.input_path, args.output_path)
    else:
        encode(args.input_path, args.output_path)

if __name__ == '__main__':
    main()
