#ifndef DATA_STRUCTURES_GRAPH_H
#define DATA_STRUCTURES_GRAPH_H

#include <cstddef>
#include <memory>
#include <vector>

namespace algorithms_archive {

struct Node {
    std::size_t id;
};

bool operator==(const Node &lhs, const Node &rhs) { return lhs.id == rhs.id; }

struct Edge {
    Node from;
    Node to;
    int weight;
};

bool operator==(const Edge &lhs, const Edge &rhs) {
    return lhs.from == rhs.from && lhs.to == rhs.to && lhs.weight == rhs.weight;
}

typedef std::vector<Edge> Path;

class AdjacencyMatrixGraph {
  public:
    AdjacencyMatrixGraph(std::size_t size);
    AdjacencyMatrixGraph(std::initializer_list<Edge> edges);
    void addEdge(const Edge &edge);

  private:
    std::size_t size_;
    std::unique_ptr<int[]> matrix_;
};

class AdjacencyListGraph {
  public:
    /**
     * Initializes an adjacency list backed graph. Size is the number of nodes
     * in the graph
     */
    AdjacencyListGraph(std::size_t size);

    /**
     * Initializes an adjacency list backed graph. Edges is a list of edges,
     * with size derived from the number of unique nodes among the edges.
     *
     * It's expected that the id's of the nodes are in the range [0, size).
     */
    AdjacencyListGraph(std::initializer_list<Edge> edges);

    void addEdge(const Edge &edge);

    std::vector<Edge> getEdges(const Node &node) const;
    std::vector<Node> getNeighbors(const Node &node);

  private:
    std::size_t size_;
    std::unique_ptr<std::vector<Edge>[]> edges_;
};

} // namespace algorithms_archive

#endif
