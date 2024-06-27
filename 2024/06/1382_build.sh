#!/bin/bash

# Set the include directory
INCLUDE_DIR="../../tree_utils/include"

# Compile the source files and link into an executable
g++ -I$INCLUDE_DIR -c ../../tree_utils/src/TreeUtils.cpp -o src/TreeUtils.o
g++ -I$INCLUDE_DIR -c 1382.cpp -o src/1382.o
g++ src/TreeUtils.o src/1382.o -o src/1382

# Run the executable
./src/1382

