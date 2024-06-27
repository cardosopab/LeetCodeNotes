// 1382. Balance a Binary Search Tree
// Medium
// Given the root of a binary search tree, return a balanced binary search tree
// with the same node values. If there is more than one answer, return any of
// them.

// A binary search tree is balanced if the depth of the two subtrees of every
// node never differs by more than 1.

#include "../../tree_utils/include/TreeNode.h"
#include "../../tree_utils/include/TreeUtils.h"
#include <iostream>
#include <optional>
#include <vector>

class Solution {
public:
  virtual TreeNode *balanceBST(TreeNode *root) = 0;
};

class Solution1 : public Solution {
public:
  std::vector<int> order;
  TreeNode *balanceBST(TreeNode *root) {
    if (!order.empty()) {
      order.clear();
    }
    dfs(root);
    return build(0, order.size() - 1);
  }

  void dfs(TreeNode *root) {
    if (!root) {
      return;
    }
    dfs(root->left);
    order.push_back(root->val);
    dfs(root->right);
  }

  TreeNode *build(int left, int right) {
    if (left > right) {
      return nullptr;
    }
    int mid = left + ((right - left) / 2);
    TreeNode *root = new TreeNode(order[mid]);
    root->left = build(left, mid - 1);
    root->right = build(mid + 1, right);
    return root;
  }
};

void test_solution(Solution *sol) {
  // Example 1:
  TreeNode *root =
      createTreeFromArray({1, std::nullopt, 2, std::nullopt, 3, std::nullopt, 4,
                           std::nullopt, std::nullopt});
  TreeNode *ans = createTreeFromArray(
      {2, 1, 3, std::nullopt, std::nullopt, std::nullopt, 4});
  TreeNode *ans1 = createTreeFromArray({3, 1, 4, std::nullopt, 2});
  TreeNode *res = sol->balanceBST(root);
  bool check = compareTrees(res, ans);
  bool check1 = compareTrees(res, ans1);
  std::cout << (check || check1 ? "Pass" : "Fail") << '\n';
  // Explanation: This is not the only correct answer, {3,1,4,std::nullopt,2} is
  // also correct.

  // Example 2:
  root = createTreeFromArray({2, 1, 3});
  ans = createTreeFromArray({2, 1, 3});
  res = sol->balanceBST(root);
  std::cout << (compareTrees(res, ans) ? "Pass" : "Fail") << '\n';

  // Constraints:
  // The number of nodes in the tree is in the range [1, 104].
  // 1 <= Node.val <= 105
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
