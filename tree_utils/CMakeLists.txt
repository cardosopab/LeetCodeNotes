cmake_minimum_required(VERSION 3.10)

# Set the project name
project(treenode)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)


# Add the include directory
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Add the executable
add_executable(tree_node ${CMAKE_CURRENT_SOURCE_DIR}/../2024/06/1038.cpp src/TreeUtils.cpp)
