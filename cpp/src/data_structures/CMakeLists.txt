set(
    HEADER_LIST
    "${AlgorithmsArchive_SOURCE_DIR}/include/algorithms_archive/data_structures/graph.h")

add_library(data_structures graph.cpp ${HEADER_LIST})
target_include_directories(data_structures PUBLIC "${AlgorithmsArchive_SOURCE_DIR}/include")

