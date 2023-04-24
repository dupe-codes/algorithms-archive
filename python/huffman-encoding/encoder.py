"""
Exports a HuffmanCoder class for encoding and decoding files.

Huffman coding is a variable-length encoding scheme based on character frequencies. 
The frequencies are used as weights to build a binary tree, with the input characters 
appearing as the tree's leaves. The tree is then traversed to build an encoding table, with 
binary codes assigned to each character. Left traverals are interpreted as adding "0" to 
a code, and right traversals as adding "1". Characters with higher frequencies appear 
at shallower levels of the tree, and thus are assigned shorter codes. Crucially, no pair 
of the resulting codes are prefixes of each other. This unique prefix property allows 
encoded files to be decoded unambiguously.

The main drawbacks of the Huffman coding scheme are:

    1. The encoding table must be stored in the encoded file, to be used later when
       decoding.

    2. The frequencies of all characters must be known in advance, which means two passes
       over the input file are required: one to count the characters, and one to encode.
"""

import heapq
import struct
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
    _HEADER_ENTRY_NUM_BYTES = 5

    def __init__(self) -> None:
        self._encoding_tree: typing.Optional[HuffmanNode] = None
        self._encoding_table: dict[str, str] = {}
        self._character_counts: dict[str, int] = {}

    def _count_characters(self, input: str) -> None:
        for character in input:
            self._character_counts[character] = self._character_counts.get(
                character, 0) + 1

    def _build_encoding_tree(self) -> None:
        # Include a pseudo EOF character in the encoding tree, which we'll use to
        # mark the end of the encoded data
        heap = [HuffmanNode(HuffmanEncoder._PSEUDO_EOF, 0)]
        for character, count in self._character_counts.items():
            heapq.heappush(heap, HuffmanNode(character, count))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            heapq.heappush(heap, HuffmanNode(
                None, left.count + right.count, left, right))

        self._encoding_tree = heap[0]

    def _build_encoding_table(self) -> None:
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

        The header is first the number of bytes used to store the encoding table, 
        then the table itself, and finally the encoding for _PSEUDO_EOF. 
        The encoding table is needed later to decode the data.

        The encoding table is written as packed bytes. This is more space efficient
        than using a JSON string, and avoids the security risks of pickling.
        """

        # Remove pseudo EOF character from encoding table
        pseudo_eof_encoding = self._encoding_table.pop(
            HuffmanEncoder._PSEUDO_EOF)

        num_items = len(self._encoding_table)
        output.write(struct.pack('>I', num_items))
        for ch, encoding in self._encoding_table.items():
            output.write(struct.pack('>BI', ord(ch), len(encoding)))
            output.write(encoding.encode())

        # Write the pseudo EOF character. Use -1 as a placeholder
        output.write(struct.pack('>iB', -1, len(pseudo_eof_encoding)))
        output.write(pseudo_eof_encoding.encode())

        # Add the pseudo EOF character back to the encoding table
        self._encoding_table[HuffmanEncoder._PSEUDO_EOF] = pseudo_eof_encoding

    def _write_encoded_data(self, input_file: typing.TextIO, output_file: typing.BinaryIO) -> None:
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
        num_items = struct.unpack('>I', input_encoded_file.read(
            HuffmanEncoder._HEADER_LENGTH_NUM_BYTES))[0]
        self._encoding_table = {}
        for _ in range(num_items):
            ch_ord, encoding_length = struct.unpack(
                '>BI', input_encoded_file.read(HuffmanEncoder._HEADER_ENTRY_NUM_BYTES))
            encoding = input_encoded_file.read(encoding_length).decode()
            self._encoding_table[encoding] = chr(ch_ord)

        # Read the pseudo EOF character, encoded in the bytes directly after the rest
        # of the encoding table
        eof_placeholder, eof_encoding_length = struct.unpack(
            '>iB', input_encoded_file.read(HuffmanEncoder._HEADER_ENTRY_NUM_BYTES))
        if eof_placeholder == -1:
            eof_encoding = input_encoded_file.read(
                eof_encoding_length).decode()
            self._encoding_table[eof_encoding] = HuffmanEncoder._PSEUDO_EOF

    def _write_decoded_data(self, input: typing.BinaryIO, output: typing.TextIO) -> None:
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
