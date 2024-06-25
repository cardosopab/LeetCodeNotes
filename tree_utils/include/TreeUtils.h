#ifndef TREE_UTILS_H
#define TREE_UTILS_H

#include "TreeNode.h"
#include <optional>
#include <vector>

TreeNode *createTreeFromArray(const std::vector<std::optional<int>> &list);
bool compareTrees(TreeNode *root1, TreeNode *root2);

#endif
