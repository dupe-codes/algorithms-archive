#include <cstddef>
#include <memory>

namespace algorithms_archive {

struct Node {
    std::size_t id;
};

struct Edge {
    Node from;
    Node to;
    int weight;
};

class AdjacencyMatrixGraph {
  public:
    AdjacencyMatrixGraph(std::size_t size);
    AdjacencyMatrixGraph(std::initializer_list<Edge> edges);
    void addEdge(const Edge &edge);

  private:
    std::size_t size_;
    std::unique_ptr<int[]> matrix_;
};

} // namespace algorithms_archive
