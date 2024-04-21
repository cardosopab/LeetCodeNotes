// 1971. Find if Path Exists in Graph
// Easy
// Topics
// Companies
// There is a bi-directional graph with n vertices, where each vertex is labeled
// from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
// integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
// edge between vertex ui and vertex vi. Every vertex pair is connected by at
// most one edge, and no vertex has an edge to itself.

// You want to determine if there is a valid path that exists from vertex source
// to vertex destination.

// Given edges and the integers n, source, and destination, return true if there
// is a valid path from source to destination, or false otherwise.

#include <deque>
#include <iostream>
#include <ostream>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
  bool validPath(int n, vector<vector<int>> &edges, int source,
                 int destination) {
    vector<vector<int>> graph(n);
    for (auto e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }

    vector<int> visited(n, 0);
    return dfs(edges, graph, visited, source, destination);
  }
  bool dfs(vector<vector<int>> &edges, vector<vector<int>> &graph,
           vector<int> &visited, int curr, int end) {
    if (curr == end) {
      return true;
    }
    if (visited[curr]) {
      return false;
    }

    visited[curr] = 1;

    for (int e : graph[curr]) {
      if (dfs(edges, graph, visited, e, end)) {
        return true;
      }
    }
    return false;
  }
};

void testValidPath() {
  Solution sol;

  // Example 1
  int n1 = 3;
  int source1 = 0;
  int destination1 = 2;
  vector<vector<int>> edges1 = {{0, 1}, {1, 2}, {2, 0}};
  bool ans1 = true;
  bool result1 = sol.validPath(n1, edges1, source1, destination1);
  cout << "Example 1: " << (result1 == ans1 ? "Pass" : "Fail") << endl;
  // Explanation: There are two paths from vertex 0 to vertex 2:
  // - 0 → 1 → 2
  // - 0 → 2

  // Example 2:
  int n2 = 6;
  int source2 = 0;
  int destination2 = 5;
  vector<vector<int>> edges2 = {{0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}};
  bool ans2 = false;
  bool result2 = sol.validPath(n2, edges2, source2, destination2);
  cout << "Example 2: " << (result2 == ans2 ? "Pass" : "Fail") << endl;
  // Explanation: There is no path from vertex 0 to vertex 5.

  // Example 3:
  int n3 = 10;
  int source3 = 5;
  int destination3 = 9;
  vector<vector<int>> edges3 = {{4, 3}, {1, 4}, {4, 8}, {1, 7}, {6, 4},
                                {4, 2}, {7, 4}, {4, 0}, {0, 9}, {5, 4}};
  bool ans3 = true;
  bool result3 = sol.validPath(n3, edges3, source3, destination3);
  cout << "Example 3: " << (result3 == ans3 ? "Pass" : "Fail") << endl;

  // Constraints:
  // 1 <= n <= 2 * 105
  // 0 <= edges.length <= 2 * 105
  // edges[i].length == 2
  // 0 <= ui, vi <= n - 1
  // ui != vi
  // 0 <= source, destination <= n - 1
  // There are no duplicate edges.
  // There are no self edges.
}
class Solution2 {
public:
  bool validPath(int n, vector<vector<int>> &edges, int source,
                 int destination) {
    vector<vector<int>> graph(n);
    for (auto e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }
    vector<int> visited(n, 0);
    deque<int> q;
    visited.push_back(source);
    q.push_back(source);

    while (q.size() > 0) {
      int node = q[0];
      q.pop_front();

      for (auto edge : graph[node]) {
        if (!visited[edge]) {
          visited[edge] = 1;
          q.push_back(edge);
        }
      }
    }

    return visited[destination];
  }
};

void testValidPath2() {
  Solution2 sol;

  // Example 1
  int n1 = 3;
  int source1 = 0;
  int destination1 = 2;
  vector<vector<int>> edges1 = {{0, 1}, {1, 2}, {2, 0}};
  bool ans1 = true;
  bool result1 = sol.validPath(n1, edges1, source1, destination1);
  cout << "Example 1: " << (result1 == ans1 ? "Pass" : "Fail") << endl;
  // Explanation: There are two paths from vertex 0 to vertex 2:
  // - 0 → 1 → 2
  // - 0 → 2

  // Example 2:
  int n2 = 6;
  int source2 = 0;
  int destination2 = 5;
  vector<vector<int>> edges2 = {{0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}};
  bool ans2 = false;
  bool result2 = sol.validPath(n2, edges2, source2, destination2);
  cout << "Example 2: " << (result2 == ans2 ? "Pass" : "Fail") << endl;
  // Explanation: There is no path from vertex 0 to vertex 5.

  // Example 3:
  int n3 = 10;
  int source3 = 5;
  int destination3 = 9;
  vector<vector<int>> edges3 = {{4, 3}, {1, 4}, {4, 8}, {1, 7}, {6, 4},
                                {4, 2}, {7, 4}, {4, 0}, {0, 9}, {5, 4}};
  bool ans3 = true;
  bool result3 = sol.validPath(n3, edges3, source3, destination3);
  cout << "Example 3: " << (result3 == ans3 ? "Pass" : "Fail") << endl;
}

int main() {
  testValidPath();
  testValidPath2();
  return 0;
}
