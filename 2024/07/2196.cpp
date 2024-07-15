// 2196. Create Binary Tree From Descriptions
// Medium
// You are given a 2D integer array descriptions where descriptions[i] =
// [parenti, childi, isLefti] indicates that parenti is the parent of childi in
// a binary tree of unique values. Furthermore,

// If isLefti == 1, then childi is the left child of parenti.
// If isLefti == 0, then childi is the right child of parenti.
// Construct the binary tree described by descriptions and return its root.

// The test cases will be generated such that the binary tree is valid.

// Definition for a binary tree node.

#include "../../tree_utils/include/TreeNode.h"
#include "../../tree_utils/include/TreeUtils.h"
#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
  virtual TreeNode *
  createBinaryTree(std::vector<std::vector<int>> &descriptions) = 0;
};

class Solution1 : public Solution {
public:
  TreeNode *createBinaryTree(std::vector<std::vector<int>> &descriptions) {
    std::unordered_map<int, TreeNode *> nodes;
    std::unordered_map<int, bool> has_parent;

    for (auto &d : descriptions) {
      auto parent = d[0], child = d[1], is_left = d[2];

      nodes.try_emplace(parent, new TreeNode(parent));
      nodes.try_emplace(child, new TreeNode(child));

      if (is_left) {
        nodes[parent]->left = nodes[child];
      } else {
        nodes[parent]->right = nodes[child];
      }
      has_parent[child] = true;
    }
    for (auto &[val, node] : nodes) {
      if (!has_parent[val]) {
        return node;
      }
    }
    return nullptr;
  };
};

void test_solution(Solution *sol) {
  // Example 1 :
  std::vector<std::vector<int>> descriptions = {
      {20, 15, 1}, {20, 17, 0}, {50, 20, 1}, {50, 80, 0}, {80, 19, 1}};
  TreeNode *ans = createTreeFromArray({50, 20, 80, 15, 17, 19});
  TreeNode *res = sol->createBinaryTree(descriptions);
  bool check = compareTrees(ans, res);
  std::cout << (check ? "Pass" : "Fail") << '\n';
  // Explanation : The root node is the node with value 50 since it has no
  // parent.The resulting binary tree is shown in the diagram.

  // Example 2 :
  descriptions = {{1, 2, 1}, {2, 3, 0}, {3, 4, 1}};
  ans = createTreeFromArray({1, 2, NULL, NULL, 3, 4});
  res = sol->createBinaryTree(descriptions);
  std::cout << (check ? "Pass" : "Fail") << '\n';
  // Explanation: The root node is the node with value 1 since it has no
  // parent.The resulting binary tree is shown in the diagram.

  // Constraints:
  // 1 <= descriptions.length <= 104
  // descriptions[i].length == 3
  // 1 <= parenti, childi <= 105
  // 0 <= isLefti <= 1
}
int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
