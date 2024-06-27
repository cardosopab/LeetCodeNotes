// 1791. Find Center of Star Graph
// Easy
// There is an undirected star graph consisting of n nodes labeled from 1 to n.
// A star graph is a graph where there is one center node and exactly n - 1
// edges that connect the center node with every other node.

// You are given a 2D integer array edges where each edges[i] = [ui, vi]
// indicates that there is an edge between the nodes ui and vi. Return the
// center of the given star graph.

#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
  virtual int findCenter(std::vector<std::vector<int>> &edges) = 0;
};

class Solution1 : public Solution {
public:
  int findCenter(std::vector<std::vector<int>> &edges) {
    std::unordered_map<int, int> count;
    for (auto e : edges) {
      if (count[e[0]]++) {
        return e[0];
      }
      if (count[e[1]]++) {
        return e[1];
      }
    }
    return 0;
  };
};

class Solution2 : public Solution {
public:
  int findCenter(std::vector<std::vector<int>> &edges) {
    std::unordered_map<int, int> count;
    int max_k = 0, max_v = 0;
    for (auto e : edges) {
      count[e[0]]++;
      count[e[1]]++;
    }
    for (auto i = count.begin(); i != count.end(); i++) {
      if (i->second > max_v) {
        max_k = i->first;
        max_v = i->second;
      }
    }
    return max_k;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<std::vector<int>> edges = {{1, 2}, {2, 3}, {4, 2}};
  int ans = 2;
  int res = sol->findCenter(edges);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: As shown in the figure above, node 2 is connected to every
  // other node, so 2 is the center.

  // Example 2:
  edges = {{1, 2}, {5, 1}, {1, 3}, {1, 4}};
  ans = 1;
  res = sol->findCenter(edges);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';

  // Constraints:
  // 3 <= n <= 105
  // edges.length == n - 1
  // edges[i].length == 2
  // 1 <= ui, vi <= n
  // ui != vi
  // The given edges represent a valid star graph.
}

int main() {
  std::cout << "Test 1" << '\n';
  Solution1 sol1;
  test_solution(&sol1);

  std::cout << "Test 2" << '\n';
  Solution2 sol2;
  test_solution(&sol2);
}
