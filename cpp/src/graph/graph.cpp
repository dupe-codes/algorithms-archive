#include <cstddef>
#include <memory>

#include "algorithms_archive/graph/graph.h"

using namespace algorithms_archive::graph;

AdjacencyMatrixGraph::AdjacencyMatrixGraph(std::size_t size)
    : size_{size}, matrix_{std::unique_ptr<int[]>{new int[size * size]}} {}

AdjacencyMatrixGraph::AdjacencyMatrixGraph(std::initializer_list<Edge> edges)
    : AdjacencyMatrixGraph{edges.size()} {
    for (const auto &edge : edges) {
        addEdge(edge);
    }
}

void AdjacencyMatrixGraph::addEdge(const Edge &edge) {
    matrix_[edge.from.id * size_ + edge.to.id] = edge.weight;
}
