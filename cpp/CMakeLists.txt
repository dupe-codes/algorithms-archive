cmake_minimum_required(VERSION 3.14...3.26)

project(
    AlgorithmsArchive
    VERSION 0.1
    DESCRIPTION "A collection of algorithms and data structures"
    LANGUAGES CXX)

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)

    # Optionally set things like CMAKE_CXX_STANDARD, CMAKE_POSITION_INDEPENDENT_CODE here
    set(CMAKE_CXX_STANDARD 20)

    # Let's ensure -std=c++xx instead of -std=g++xx
    set(CMAKE_CXX_EXTENSIONS OFF)

    # Export compile commands so that ccls language server can use them
    # After running initializing cmake, run `ln -s build/compile_commands.json compile_commands.json`
    # in the project root
    set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

    # Testing only available if this is the main app
    include(CTest)

endif()

include(FetchContent)

# Add subdirectories
add_subdirectory(src)
add_subdirectory(demos)

# Testing only available if this is the main app
if((CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME) AND BUILD_TESTING)
  add_subdirectory(tests)
endif()

# Set flags for debug builds
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    add_compile_options(-Wall -Wextra -pedantic -Werror)
endif()

