#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <algorithms_archive/binary_search/search.h>

TEST_CASE( "Quick check", "[main]" ) {
    int num_elements = 10;
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9 ,10};
    int find = 3;
    int index = binary_search::search(arr, num_elements, find);
    REQUIRE( index == 2 );
}

