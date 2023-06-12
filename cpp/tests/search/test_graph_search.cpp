#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>

#include "algorithms_archive/search/graph.h"

using namespace algorithms_archive;

TEST_CASE("Basic BFS", "[main]") {
    AdjacencyListGraph graph{
        {Node{0}, Node{1}}, {Node{0}, Node{2}}, {Node{1}, Node{3}},
        {Node{2}, Node{3}}, {Node{3}, Node{4}},
    };

    Node start{0};
    Node end{4};

    // FIXME: This reference can't be found when compiling...
    // Path actualPath = bfs(graph, start, end);
    // Path expectedPath{
    // Edge{Node{0}, Node{1}},
    // Edge{Node{1}, Node{3}},
    // Edge{Node{3}, Node{4}},
    //};
    // REQUIRE(actualPath == expectedPath);
}
