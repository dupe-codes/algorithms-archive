"""
This module implements a Huffman encoder and decoder for compressing
and decompressing files.
"""
class HuffmanEncoder:

    def __init__(self) -> None:
        """
        Initializes a new Huffman encoder.
        """
        self._encoding_tree: list[tuple[str, int]] = []
        self._encoding_table: dict[str, str] = {}
        self._character_counts: dict[str, int] = {}

    def _count_characters(self, input: list[str]) -> None:
        """
        Counts the number of times each character appears in the given input.
        """
        for line in input:
            for character in line:
                self._character_counts[character] = self._character_counts.get(character, 0) + 1

    def _build_encoding_tree(self) -> None:
        """
        Builds the encoding tree from the character counts.
        """
        pass

    def _build_encoding_table(self) -> None:
        """
        Builds the encoding table from the encoding tree.
        """
        pass

    def fit_encoder(self, input: list[str]) -> None:
        """
        Fits the encoder to the given input.
        """
        self._count_characters(input)
        self._build_encoding_tree()
        self._build_encoding_table()

    def fit_decoder(self, input: list[str]) -> None:
        """
        Fits the decoder to the given input.
        """
        pass

    def encode(self, input: list[str]) -> list[str]:
        print('Encoding...')
        return [':)']

    def decode(self, input: list[str]) -> list[str]:
        print('Decoding...')
        return [':)']
