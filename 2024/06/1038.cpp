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

#include "../../tree_utils/include/TreeNode.h"
#include "../../tree_utils/include/TreeUtils.h"
#include <iostream>
#include <optional>
#include <vector>

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
