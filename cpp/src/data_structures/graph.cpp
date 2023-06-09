#include <cstddef>
#include <memory>
#include <set>

#include "algorithms_archive/data_structures/graph.h"

using namespace algorithms_archive;

AdjacencyMatrixGraph::AdjacencyMatrixGraph(std::size_t size)
    : size_{size}, matrix_{std::unique_ptr<int[]>{new int[size * size]}} {}

AdjacencyMatrixGraph::AdjacencyMatrixGraph(std::initializer_list<Edge> edges) {
    // count number of unique nodes in the given edges list
    std::set<int> nodes;
    for (const auto &edge : edges) {
        nodes.insert(edge.from.id);
        nodes.insert(edge.to.id);
    }

    size_ = nodes.size();
    matrix_ = std::unique_ptr<int[]>{new int[size_ * size_]};
    for (const auto &edge : edges) {
        addEdge(edge);
    }
}

void AdjacencyMatrixGraph::addEdge(const Edge &edge) {
    matrix_[edge.from.id * size_ + edge.to.id] = edge.weight;
}
