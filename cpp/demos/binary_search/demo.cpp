#include "algorithms_archive/binary_search/search.h"
#include <iostream>

int main() {
    int num_elements = 5;
    int arr[] = {1, 2, 3, 4, 5};
    int target = 3;
    int result = binary_search::search(arr, num_elements, target);
    std::cout << "result: " << result << std::endl;
    return 0;
}
