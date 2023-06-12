set(
    HEADER_LIST
    "${AlgorithmsArchive_SOURCE_DIR}/include/algorithms_archive/search/graph.h")

add_library(search graph.cpp ${HEADER_LIST})
target_include_directories(search PUBLIC "${AlgorithmsArchive_SOURCE_DIR}/include")
target_link_libraries(search PRIVATE data_structures)
