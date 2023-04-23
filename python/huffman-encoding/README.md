# File Compression with Huffman Coding

A simple command line utility for compressing files using the Huffman coding scheme. 

`èncoder.py` exports a `HuffmanCoder` class that implements encoding and decoding. 
`huff_zip.py` makes use of this class to implement its compression utilities.

## Usage

To encode an input file:

```
./huff_zip.py input.txt output.huff
```

To decode an encoded file:

```
./huff_zip.py output.huff input_decoded.txt
```

Note that attempting to decode a file that was _not_ actually encoded with HuffmanCoder#encode
will error

