// 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
// Hard
// Alice and Bob have an undirected graph of n nodes and three types of edges:

// Type 1: Can be traversed by Alice only.
// Type 2: Can be traversed by Bob only.
// Type 3: Can be traversed by both Alice and Bob.
// Given an array edges where edges[i] = [typei, ui, vi] represents a
// bidirectional edge of type typei between nodes ui and vi, find the maximum
// number of edges you can remove so that after removing the edges, the graph
// can still be fully traversed by both Alice and Bob. The graph is fully
// traversed by Alice and Bob if starting from any node, they can reach all
// other nodes.

// Return the maximum number of edges you can remove, or return -1 if Alice and
// Bob cannot fully traverse the graph.

#include <iostream>
#include <vector>

class UnionFind {
  int *parent;
  int N;

public:
  UnionFind(int n) {
    N = n;
    parent = new int[N];
    for (int i = 0; i < N; i++) {
      parent[i] = i;
    }
  }

  int find(int x) {
    int root = x;
    while (parent[root] != root) {
      root = parent[root];
    }
    return root;
  }

  void merge(int x, int y) {
    int root_x = find(x);
    int root_y = find(y);

    if (root_x != root_y) {
      parent[root_x] = root_y;
    }
  }

  bool is_connected(int x, int y) { return find(x) == find(y); }
};

class Solution {
public:
  virtual int maxNumEdgesToRemove(int n,
                                  std::vector<std::vector<int>> &edges) = 0;
};

class Solution1 : public Solution {
public:
  int maxNumEdgesToRemove(int n, std::vector<std::vector<int>> &edges) {
    auto alice = UnionFind(n);
    auto bob = UnionFind(n);
    int ans = 0;

    for (const auto &e : edges) {
      int v = e[0], x = e[1], y = e[2];
      x--;
      y--;
      if (v == 3) {
        if (alice.is_connected(x, y)) {
          ans++;
        } else {
          alice.merge(x, y);
          bob.merge(x, y);
        }
      }
    }

    for (const auto &e : edges) {
      int v = e[0], x = e[1], y = e[2];
      x--;
      y--;
      if (v == 1) {
        if (alice.is_connected(x, y)) {
          ans++;
        } else {
          alice.merge(x, y);
        }
      }
    }

    for (const auto &e : edges) {
      int v = e[0], x = e[1], y = e[2];
      x--;
      y--;
      if (v == 2) {
        if (bob.is_connected(x, y)) {
          ans++;
        } else {
          bob.merge(x, y);
        }
      }
    }

    for (int i = 0; i < n; i++) {
      if (!alice.is_connected(0, i) || !alice.is_connected(0, i)) {
        return -1;
      }
    }

    return ans;
  }
};

void test_solution(Solution *sol) {
  // Example 1:
  int n = 4;
  std::vector<std::vector<int>> edges = {{3, 1, 2}, {3, 2, 3}, {1, 1, 3},
                                         {1, 2, 4}, {1, 1, 2}, {2, 3, 4}};
  int ans = 2;
  int res = sol->maxNumEdgesToRemove(n, edges);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: If we remove the 2 edges {1,1,2} and {1,1,3}. The graph will
  // still be fully traversable by Alice and Bob. Removing any additional edge
  // will not make it so. So the maximum number of edges we can remove is 2.

  // Example 2:
  n = 4;
  edges = {{3, 1, 2}, {3, 2, 3}, {1, 1, 4}, {2, 1, 4}};
  ans = 0;
  res = sol->maxNumEdgesToRemove(n, edges);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: Notice that removing any edge will not make the graph fully
  // traversable by Alice and Bob.

  // Example 3:
  n = 4;
  edges = {{3, 2, 3}, {1, 1, 2}, {2, 3, 4}};
  ans = -1;
  res = sol->maxNumEdgesToRemove(n, edges);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: In the current graph, Alice cannot reach node 4 from the
  // other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to
  // make the graph fully traversable.

  // Constraints:
  // 1 <= n <= 105
  // 1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
  // edges{i}.length == 3
  // 1 <= typei <= 3
  // 1 <= ui < vi <= n
  // All tuples (typei, ui, vi) are distinct.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
