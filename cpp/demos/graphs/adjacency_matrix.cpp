#include <iostream>

#include "algorithms_archive/graph/graph.h"

using namespace algorithms_archive::graph;

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
