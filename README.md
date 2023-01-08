# Algorithms & Data Structures Archive

Implementations and notes on interesting algorithms, data structures, and other CS stuff


# TODO list

- Hashing:
    - Build a framework for grabbing a hash function from a
      desired hash family
        - model after 166 problem set
    - Linear probing hash table (rust? java?)
    - Robin hood Hashing
    - Cuckoo Hashing
    - Classic chaining hash table
    - Dynamic FKS hashing

- Randomized Data Structures:
    - Bloom Filter
    - Quotient Filter
    - Count sketch
    - Count-min sketch (finish)
    - Tug-of-War sketch
    - Group tester for k-heavy hitters

- Heaps
    - Binomial Heap (rust)
        - + Lazy Binomial Heap
    - Fibonacci heap (rust)
    - Soft Heap
    - Shadow Heap
    - Pairing heap
    - Brodal queue
    - Treap
    - Heap w/ efficient add-to-all functionality

- Trees
    - Splay Tree
        - w/ normal recursive splaying
        - w/ top-down splaying
    - Red-Black Tree
        - with split and join operations
        - Maybe make easy to augment Red-Black Tree ?
    - AVL Tree
    - B-Tree
    - B+-Tree
    - Fusion Tree
    - Kd-tree
    - Segment Tree
    - Tango Tree
    - Trie
    - Finger tree
    - Euler Tour Trees
    - Link/cut trees
    - Weight balanced Trees
    - Knuth O(n^2) alg for constructing statically optimal BSTs
    - Multisplay Trees
    - Online greedy BSTs

- Integers
    - x-Fast trie
    - y-Fast trie
    - van Emde Boas tree

- Strings
    - Suffix Tree (Ukkonen's Algorithm)
    - DAWG
    - Suffix Array (DC3 Algorithm)
    - Aho Corasick Automaton
    - Knuth-Morris-Pratt Algorithm
    - k-approximate matching
    - Boyer-Moore Algorithm
    - Commentz-Waltz Algorithm
    - Longest Repeated Substring problem
    - Longest common substring
    - Kasai's LCP algorithm
    - Farach's Algorithm
    - Factor Oracle
    - Burrows-Wheeler Transform

- Skip List
    - + Deterministic skip list (1-2-3 skip list)
- Fischer-Heun RMQ Structure

- Max Flow Algorithms
    - push-relabel
    - Dinic's algorithm
    - Edmonds-Karp
    - Ford-Fulkerson

- Multiplicative weights Algorithm (Java)
    - + a framework for "online" problems (Java)

- Graphs:
    - Disjoint set data Structure
    - Topological Sort
    - Christofide's TSP approximation Algorithm
    - Hungarian Algorithm (for min-cost perfect matching)
    - Various Graph Algorithms
        - Dijkstra's
        - Kruskal's
        - Prim's
        - Chu-Liu-Edmonds directed graph MSY algorithm

- Sorting
    - Radix Sort
    - The usuals (quick, heap, merge)

- Misc.
    - PageRank

# Misc. Ideas
- Make interface for Graphs
    - then implement data structures that adhere to that interface
    - this will make coding graph algorithms easier :)
- Build a platform for running performance benchmark testing on data structures/algorithms
    - Could this be done programming language agnostic?

# Things to lookup and learn


- Functional Programming
- Tabulation Hashing
- How to generate multiple hash functions
- Purely functional data structures
    - In hand, persistent data structures
- Geometric data structures
- Concurrent data structures
- Dynamically optimal BSTs
- Cardinality Estimators
- Random Graph Theory
- Logical Data Structures
    - Boolean Expression Diagrams
    - Zero-suppressed decision diagrams
- Push-down automata
