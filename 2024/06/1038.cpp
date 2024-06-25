// 1038. Binary Search Tree to Greater Sum Tree
// Medium
// Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
// such that every key of the original BST is changed to the original key plus
// the sum of all keys greater than the original key in BST.

// As a reminder, a binary search tree is a tree that satisfies these
// constraints:

// The left subtree of a node contains only nodes with keys less than the node's
// key. The right subtree of a node contains only nodes with keys greater than
// the node's key. Both the left and right subtrees must also be binary search
// trees.

#include <cstddef>
#include <iostream>
#include <optional>
#include <vector>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  virtual TreeNode *bstToGst(TreeNode *root) = 0;
  virtual void dfs(TreeNode *root) = 0;
};

class Solution1 : public Solution {
public:
  int ans = 0;
  TreeNode *bstToGst(TreeNode *root) {
    ans = 0;
    dfs(root);
    return root;
  }
  void dfs(TreeNode *root) {
    if (root == nullptr) {
      return;
    }
    dfs(root->right);
    this->ans += root->val;
    root->val = this->ans;
    dfs(root->left);
  }
};

TreeNode *createTreeFromArray(const std::vector<std::optional<int>> &list) {
  if (list.empty() || !list[0].has_value()) {
    return nullptr;
  }

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
      if (2 * i + 1 < nodes.size()) {
        nodes[i]->left = nodes[2 * i + 1];
      }
      if (2 * i + 2 < nodes.size()) {
        nodes[i]->right = nodes[2 * i + 2];
      }
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

void test_solution(Solution *sol) {
  // Example 1:
  TreeNode *root = createTreeFromArray(
      {4, 1, 6, 0, 2, 5, 7, std::nullopt, std::nullopt, std::nullopt, 3,
       std::nullopt, std::nullopt, std::nullopt, 8});
  TreeNode *ans = createTreeFromArray(
      {30, 36, 21, 36, 35, 26, 15, std::nullopt, std::nullopt, std::nullopt, 33,
       std::nullopt, std::nullopt, std::nullopt, 8});
  TreeNode *res = sol->bstToGst(root);
  std::cout << (compareTrees(res, ans) ? "Pass" : "Fail") << '\n';

  // Example 2:
  root = createTreeFromArray({0, std::nullopt, 1});
  ans = createTreeFromArray({1, std::nullopt, 1});
  res = sol->bstToGst(root);
  std::cout << (compareTrees(res, ans) ? "Pass" : "Fail") << '\n';

  // Constraints:
  // The number of nodes in the tree is in the range {1, 100}.
  // 0 <= Node.val <= 100
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
