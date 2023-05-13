set(
    HEADER_LIST
    "${AlgorithmsArchive_SOURCE_DIR}/include/algorithms_archive/binary_search/search.h")

add_library(binary_search search.cpp ${HEADER_LIST})

target_include_directories(binary_search PUBLIC ../../include)

# target_compile_features(binary_search PUBLIC cxx_std_20)

