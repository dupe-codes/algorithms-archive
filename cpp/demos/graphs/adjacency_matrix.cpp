#include <iostream>

#include "algorithms_archive/data_structures/graph.h"

using namespace algorithms_archive;

int main() {
    AdjacencyMatrixGraph graph = {
        Edge{Node{0}, Node{1}, 1},
        Edge{Node{0}, Node{2}, 2},
        Edge{Node{1}, Node{2}, 3},
        Edge{Node{2}, Node{0}, 4},
    };

    std::cout << "Done!" << std::endl;
    return 0;
}
