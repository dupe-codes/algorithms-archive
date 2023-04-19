"""
This module implements a Huffman encoder and decoder for compressing
and decompressing files.
"""

import heapq
import json
import typing


class HuffmanNode:

    def __init__(self,
                 character: typing.Optional[str],
                 count: int,
                 left: typing.Optional['HuffmanNode'] = None,
                 right: typing.Optional['HuffmanNode'] = None) -> None:
        self.character = character
        self.count = count
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'HuffmanNode({self.character}, {self.count})'

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.count < other.count

    def __eq__(self, other: 'HuffmanNode') -> bool:
        return self.count == other.count

    def __gt__(self, other: 'HuffmanNode') -> bool:
        return self.count > other.count


class HuffmanEncoder:

    _PSEUDO_EOF = 'EOF'
    _BYTE_SIZE = 8
    _HEADER_LENGTH_NUM_BYTES = 4

    def __init__(self) -> None:
        """
        Initializes a new Huffman encoder.
        """
        self._encoding_tree: typing.Optional[HuffmanNode] = None
        self._encoding_table: dict[str, str] = {}
        self._character_counts: dict[str, int] = {}

    def _count_characters(self, input: str) -> None:
        """ Counts the number of times each character appears in the given input. """
        for character in input:
            self._character_counts[character] = self._character_counts.get(
                character, 0) + 1

    def _build_encoding_tree(self) -> None:
        """
        Builds the encoding tree from the character counts.
        """
        heap = [HuffmanNode(HuffmanEncoder._PSEUDO_EOF, 0)]
        for character, count in self._character_counts.items():
            # Use negative counts so larger counts are at the top of the heap
            heapq.heappush(heap, HuffmanNode(character, count))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            heapq.heappush(heap, HuffmanNode(
                None, left.count + right.count, left, right))

        self._encoding_tree = heap[0]

    def _build_encoding_table(self) -> None:
        """
        Builds the encoding table from the encoding tree.
        """

        stack = []
        stack.append((self._encoding_tree, ''))
        while len(stack) > 0:
            node, code = stack.pop()
            if node.character is not None:
                self._encoding_table[node.character] = code
            else:
                stack.append((node.left, code + '0'))
                stack.append((node.right, code + '1'))

    def _fit_encoder(self, input_file: str) -> None:
        """
        Fits the encoder to the given input.
        """
        with open(input_file, 'r') as file:
            for line in file:
                self._count_characters(line)
        self._build_encoding_tree()
        self._build_encoding_table()

    def _write_header(self, output: typing.BinaryIO) -> None:
        """
        Writes the header to the given output file.

        The header is first the number of bytes used for the encoding table followed
        by the table table itself. The encoding table is needed later to decode the 
        data.
        """

        # Write the encoding table as a json string, which is more secure
        # than pickling
        encoding_table_json = json.dumps(self._encoding_table)
        encoding_table_num_bytes = len(encoding_table_json)

        output.write(encoding_table_num_bytes.to_bytes(
            HuffmanEncoder._HEADER_LENGTH_NUM_BYTES, 'big'))
        output.write(encoding_table_json.encode())

    def _write_encoded_data(self, input_file: typing.TextIO, output_file: typing.BinaryIO) -> None:
        """
        Writes the encoded data to the given output file.
        """
        def write_chunk(chunk: str, output_file: typing.BinaryIO) -> str:
            if len(chunk) == HuffmanEncoder._BYTE_SIZE:
                output_file.write(bytearray([int(chunk, 2)]))
                return ''
            return chunk

        chunk = ''
        for line in input_file:
            encoded_line = ''.join(self._encoding_table[char] for char in line)

            for encoded_char in encoded_line:
                chunk += encoded_char
                chunk = write_chunk(chunk, output_file)

        # Append the pseudo EOF character
        pseudo_eof_encoded = self._encoding_table[HuffmanEncoder._PSEUDO_EOF]
        for bit in pseudo_eof_encoded:
            chunk += bit
            chunk = write_chunk(chunk, output_file)

        if len(chunk) > 0:
            chunk = chunk.ljust(HuffmanEncoder._BYTE_SIZE, '0')
            output_file.write(bytearray([int(chunk, 2)]))

    def _fit_decoder(self, input_encoded_file: typing.BinaryIO) -> None:
        """
        Fits the decoder to the given input. 

        The decoder is fit by reading the encoding table from the header of the file.
        After this method completes, the open input file will be at the start of the
        encoded data, ready for decoding.
        """
        encoding_table_num_bytes = int.from_bytes(
            input_encoded_file.read(HuffmanEncoder._HEADER_LENGTH_NUM_BYTES), 'big')
        encoding_table_json = input_encoded_file.read(
            encoding_table_num_bytes).decode()

        # Decode the encoding table and reverse it for quick encoded -> original
        # lookups
        self._encoding_table = {
            v: k
            for k, v in json.loads(encoding_table_json).items()
        }

    def _write_decoded_data(self, input: typing.BinaryIO, output: typing.TextIO) -> None:
        """
        Writes the decoded data to the given output file.
        """
        def read_bits(input: typing.BinaryIO) -> typing.Generator[str, None, None]:
            for byte in iter(lambda: input.read(1), b''):
                for bit in format(ord(byte), '08b'):
                    yield bit

        current_code = ''
        for bit in read_bits(input):
            # Build the code until we find a match
            current_code += bit
            if current_code in self._encoding_table:
                decoded_char = self._encoding_table[current_code]
                if decoded_char == HuffmanEncoder._PSEUDO_EOF:
                    return
                output.write(decoded_char)
                current_code = ''

    def encode(self, input_file: str, destination: str) -> None:
        self._fit_encoder(input_file)

        with open(input_file, 'r') as file:
            with open(destination, 'wb') as output:
                self._write_header(output)
                self._write_encoded_data(file, output)

    def decode(self, input_encoded_file: str, destination: str) -> None:
        with open(input_encoded_file, 'rb') as file:
            with open(destination, 'w') as output:
                self._fit_decoder(file)
                self._write_decoded_data(file, output)
