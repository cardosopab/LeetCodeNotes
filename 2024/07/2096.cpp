
// 2096. Step-By-Step
// Directions From a Binary Tree Node to Another
// Medium
// You are given the root of a binary tree with n nodes. Each node is uniquely
// assigned a value from 1 to n. You are also given an integer startValue
// representing the value of the start node s, and a different integer destValue
// representing the value of the destination node t.

// Find the shortest path starting from node s and ending at node t. Generate
// step-by-step directions of such path as a string consisting of only the
// uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific
// direction:

// 'L' means to go from a node to its left child node.
// 'R' means to go from a node to its right child node.
// 'U' means to go from a node to its parent node.
// Return the step-by-step directions of the shortest path from node s to node
// t.

#include "../../tree_utils/include/TreeNode.h"
#include "../../tree_utils/include/TreeUtils.h"
#include <deque>
#include <iostream>
#include <vector>

class Solution {
public:
  virtual std::string getDirections(TreeNode *root, int startValue,
                                    int destValue) = 0;
};

class Solution1 : public Solution {
public:
  std::string getDirections(TreeNode *root, int startValue, int destValue) {
    auto start = std::deque<char>();
    dfs(root, start, startValue);
    auto dest = std::deque<char>();
    dfs(root, dest, destValue);
    std::string ans = "";

    while (!start.empty() && !dest.empty() && start.front() == dest.front()) {
      start.pop_front();
      dest.pop_front();
    }

    while (!start.empty()) {
      start.pop_front();
      ans += "U";
    }
    while (!dest.empty()) {
      ans += dest.front();
      dest.pop_front();
    }
    return ans;
  };

  bool dfs(TreeNode *node, std::deque<char> &path, int target) {
    if (!node || !node->val) {
      return false;
    }

    if (node->val == target) {
      return true;
    }

    path.push_back('L');
    auto left = dfs(node->left, path, target);
    if (left) {
      return true;
    }
    path.pop_back();

    path.push_back('R');
    auto right = dfs(node->right, path, target);
    if (right) {
      return true;
    }
    path.pop_back();

    return false;
  }
};

void test_solution(Solution *sol) {
  // Example 1:
  TreeNode *root = createTreeFromArray({5, 1, 2, 3, NULL, 6, 4});
  int startValue = 3;
  int destValue = 6;
  std::string ans = "UURL";
  std::string res = sol->getDirections(root, startValue, destValue);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

  // Example 2:
  root = createTreeFromArray({2, 1});
  startValue = 2;
  destValue = 1;
  ans = "L";
  res = sol->getDirections(root, startValue, destValue);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The shortest path is: 2 → 1.

  // Constraints:
  // The number of nodes in the tree is n.
  // 2 <= n <= 105
  // 1 <= Node.val <= n
  // All the values in the tree are unique.
  // 1 <= startValue, destValue <= n
  // startValue != destValue
}
int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
