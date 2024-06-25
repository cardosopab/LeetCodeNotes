#include "../include/TreeUtils.h"

TreeNode *createTreeFromArray(const std::vector<std::optional<int>> &list) {
  if (list.empty() || !list[0].has_value())
    return nullptr;

  std::vector<TreeNode *> nodes;
  for (const auto &val : list) {
    if (val.has_value()) {
      nodes.push_back(new TreeNode(val.value()));
    } else {
      nodes.push_back(nullptr);
    }
  }

  for (size_t i = 0; i < nodes.size(); ++i) {
    if (nodes[i] != nullptr) {
      if (2 * i + 1 < nodes.size())
        nodes[i]->left = nodes[2 * i + 1];
      if (2 * i + 2 < nodes.size())
        nodes[i]->right = nodes[2 * i + 2];
    }
  }
  return nodes.empty() ? nullptr : nodes[0];
}

bool compareTrees(TreeNode *root1, TreeNode *root2) {
  if (!root1 && !root2)
    return true;
  if (!root1 || !root2)
    return false;
  if (root1->val != root2->val)
    return false;
  return compareTrees(root1->left, root2->left) &&
         compareTrees(root1->right, root2->right);
}
