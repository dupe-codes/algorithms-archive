set(
    HEADER_LIST
    "${AlgorithmsArchive_SOURCE_DIR}/include/algorithms_archive/graph/graph.h")

add_library(graph graph.cpp ${HEADER_LIST})
target_include_directories(graph PUBLIC "${AlgorithmsArchive_SOURCE_DIR}/include")

