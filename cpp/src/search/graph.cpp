#include <queue>
#include <set>

#include "algorithms_archive/search/graph.h"

using namespace algorithms_archive;

Path bfs(const AdjacencyListGraph &graph, const Node &start, const Node &end) {
    std::set<size_t> visited{start.id};
    std::queue<Path> frontier;

    for (const auto &edge : graph.getEdges(start)) {
        frontier.push(Path{edge});
    }

    while (!frontier.empty()) {
        Path candidate = frontier.front();
        frontier.pop();

        if (candidate.back().to.id == end.id) {
            return candidate;
        }
        visited.insert(candidate.back().to.id);

        for (const auto &edge : graph.getEdges(candidate.back().to)) {
            if (visited.find(edge.to.id) == visited.end()) {
                // edge destination not yet visited
                Path new_path = candidate;
                new_path.push_back(edge);
                frontier.push(new_path);
            }
        }
    }

    // Empty path means no path was found
    return Path{};
}

Path dfs(const AdjacencyListGraph &graph, const Node &start, const Node &end) {
    return Path{};
}

Path dijkstra(const AdjacencyListGraph &graph, const Node &start,
              const Node &end) {
    return Path{};
}
