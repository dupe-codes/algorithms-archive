#ifndef SEARCH_GRAPH_H
#define SEARCH_GRAPH_H

#include "algorithms_archive/data_structures/graph.h"

namespace algorithms_archive {

Path bfs(const AdjacencyListGraph &graph, const Node &start, const Node &end);

Path dfs(const AdjacencyListGraph &graph, const Node &start, const Node &end);

Path dijkstra(const AdjacencyListGraph &graph, const Node &start,
              const Node &end);

} // namespace algorithms_archive

#endif
