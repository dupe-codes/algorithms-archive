# Testing library
FetchContent_Declare(
  catch
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v2.13.6)
FetchContent_MakeAvailable(catch)
# Adds Catch2::Catch2

# Tests need to be added as executables first
add_executable(test_search test_search.cpp)

# Should be linked to the main library, as well as the Catch2 testing library
target_link_libraries(test_search PRIVATE binary_search Catch2::Catch2)

# If you register a test, then ctest and make test will run it.
# You can also run examples and check the output, as well.
add_test(NAME test_search_test COMMAND test_search) # Command can be a target

