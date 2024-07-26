// 1334. Find the City With the Smallest Number of Neighbors at a Threshold
// Distance Medium There are n cities numbered from 0 to n-1. Given the array
// edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and
// weighted edge between cities fromi and toi, and given the integer
// distanceThreshold.

// Return the city with the smallest number of cities that are reachable through
// some path and whose distance is at most distanceThreshold, If there are
// multiple such cities, return the city with the greatest number.

// Notice that the distance of a path connecting cities i and j is equal to the
// sum of the edges' weights along that path.

#include <algorithm>
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <set>
#include <unordered_map>
#include <utility>
#include <vector>
class Solution {
public:
  virtual int findTheCity(int n, std::vector<std::vector<int>> &edges,
                          int distanceThreshold) = 0;
};

class Solution1 : public Solution {
public:
  int findTheCity(int n, std::vector<std::vector<int>> &edges,
                  int distanceThreshold) {
    std::unordered_map<int, std::vector<std::pair<int, int>>> adj;
    for (const auto &edge : edges) {
      int src = edge[0], dest = edge[1], dist = edge[2];
      adj[src].emplace_back(dist, dest);
      adj[dest].emplace_back(dist, src);
    }

    int res = -1, min_cnt = n;
    for (int i = 0; i < n; i++) {
      int cnt = dijkstra(adj, i, distanceThreshold);
      if (cnt <= min_cnt) {
        res = i;
        min_cnt = cnt;
      }
    }
    return res;
  }

  int dijkstra(std::unordered_map<int, std::vector<std::pair<int, int>>> &adj,
               int src, int distanceThreshold) {
    using pii = std::pair<int, int>;
    std::priority_queue<pii, std::vector<pii>, std::greater<>> min_heap;
    std::set<int> visited;

    min_heap.emplace(0, src);

    while (!min_heap.empty()) {
      auto [dist, src] = min_heap.top();
      min_heap.pop();
      if (visited.find(src) != visited.end()) {
        continue;
      }
      visited.emplace(src);
      for (auto [nei_dist, nei] : adj[src]) {
        nei_dist += dist;
        if (nei_dist <= distanceThreshold) {
          min_heap.emplace(nei_dist, nei);
        }
      }
    }
    int size = visited.size() - 1;
    return size;
  }
};

class Solution2 : public Solution {
public:
  int findTheCity(int n, std::vector<std::vector<int>> &edges,
                  int distanceThreshold) {
    std::unordered_map<int, std::vector<std::pair<int, int>>> adj;
    for (const auto &edge : edges) {
      int src = edge[0], dest = edge[1], dist = edge[2];
      adj[src].emplace_back(dist, dest);
      adj[dest].emplace_back(dist, src);
    }

    int res = -1, min_cnt = n;
    for (int i = 0; i < n; i++) {
      int cnt = dijkstra(adj, i, distanceThreshold, n);
      if (cnt <= min_cnt) {
        res = i;
        min_cnt = cnt;
      }
    }
    return res;
  }

  int dijkstra(std::unordered_map<int, std::vector<std::pair<int, int>>> &adj,
               int src, int distanceThreshold, int n) {
    std::vector<int> stack(n, std::numeric_limits<int>::max());
    stack[src] = 0;

    using pii = std::pair<int, int>;
    std::priority_queue<pii, std::vector<pii>, std::greater<>> min_heap;
    min_heap.emplace(0, src);

    while (!min_heap.empty()) {
      auto [dist, src] = min_heap.top();
      min_heap.pop();

      if (dist > stack[src]) {
        continue;
      }

      for (auto &[nei_dist, nei] : adj[src]) {
        int new_dist = nei_dist + dist;
        if (new_dist < stack[nei] && new_dist <= distanceThreshold) {
          stack[nei] = new_dist;
          min_heap.emplace(new_dist, nei);
        }
      }
    }

    int cnt = 0;
    for (int d : stack) {
      if (d <= distanceThreshold) {
        cnt++;
      }
    }
    return cnt - 1;
  }
};

void test_solution(Solution *sol) {
  // Example 1:
  int n = 4;
  std::vector<std::vector<int>> edges = {
      {0, 1, 3}, {1, 2, 1}, {1, 3, 4}, {2, 3, 1}};
  int distanceThreshold = 4;
  int ans = 3;
  int res = sol->findTheCity(n, edges, distanceThreshold);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The figure above describes the graph.
  // The neighboring cities at a distanceThreshold = 4 for each city are:
  // City 0 -> {City 1, City 2}
  // City 1 -> {City 0, City 2, City 3}
  // City 2 -> {City 0, City 1, City 3}
  // City 3 -> {City 1, City 2}
  // Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we
  // have to return city 3 since it has the greatest number.

  // Example 2:
  n = 5;
  edges = {{0, 1, 2}, {0, 4, 8}, {1, 2, 3}, {1, 4, 2}, {2, 3, 1}, {3, 4, 1}};
  distanceThreshold = 2;
  ans = 0;
  res = sol->findTheCity(n, edges, distanceThreshold);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The figure above describes the graph.
  // The neighboring cities at a distanceThreshold = 2 for each city are:
  // City 0 -> {City 1}
  // City 1 -> {City 0, City 4}
  // City 2 -> {City 3, City 4}
  // City 3 -> {City 2, City 4}
  // City 4 -> {City 1, City 2, City 3}
  // The city 0 has 1 neighboring city at a distanceThreshold = 2.

  // Constraints:
  // 2 <= n <= 100
  // 1 <= edges.length <= n * (n - 1) / 2
  // edges{i}.length == 3
  // 0 <= fromi < toi < n
  // 1 <= weighti
  // distanceThreshold <= 10^4
  // All pairs (fromi, toi) are distinct.
}

int main() {
  std::cout << "Test 1" << '\n';
  Solution1 sol1;
  test_solution(&sol1);
  std::cout << "Test 2" << '\n';
  Solution2 sol2;
  test_solution(&sol2);
}
