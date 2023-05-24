set(
    HEADER_LIST
    "${AlgorithmsArchive_SOURCE_DIR}/include/algorithms_archive/binary_search/search.h")

add_library(binary_search search.cpp ${HEADER_LIST})

# TODO: replace relative path with "${AlgorithmsArchive_SOURCE_DIR}/include"
target_include_directories(binary_search PUBLIC ../../include)

