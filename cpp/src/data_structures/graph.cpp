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

// start: AdjanecyListGraph implementation

AdjacencyListGraph::AdjacencyListGraph(std::size_t size)
    : size_{size}, edges_{std::unique_ptr<std::vector<Edge>[]>{
                       new std::vector<Edge>[size]}} {}

AdjacencyListGraph::AdjacencyListGraph(std::initializer_list<Edge> edges) {
    // count number of unique nodes in the given edges list
    std::set<int> nodes;
    for (const auto &edge : edges) {
        nodes.insert(edge.from.id);
        nodes.insert(edge.to.id);
    }

    size_ = nodes.size();
    edges_ = std::unique_ptr<std::vector<Edge>[]>{new std::vector<Edge>[size_]};
    for (const auto &edge : edges) {
        addEdge(edge);
    }
}

void AdjacencyListGraph::addEdge(const Edge &edge) {
    edges_[edge.from.id].push_back(edge);
}

std::vector<Edge> AdjacencyListGraph::getEdges(const Node &node) const {
    return edges_[node.id];
}

std::vector<Node> AdjacencyListGraph::getNeighbors(const Node &node) {
    std::vector<Node> nodes{edges_[node.id].size()};
    for (const auto &edge : edges_[node.id]) {
        nodes.push_back(edge.to);
    }
    return nodes;
}

// end: AdjanecyListGraph implementation
