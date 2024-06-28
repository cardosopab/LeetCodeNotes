// 2285. Maximum Total Importance of Roads
// Medium
// You are given an integer n denoting the number of cities in a country. The
// cities are numbered from 0 to n - 1.

// You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes
// that there exists a bidirectional road connecting cities ai and bi.

// You need to assign each city with an integer value from 1 to n, where each
// value can only be used once. The importance of a road is then defined as the
// sum of the values of the two cities it connects.

// Return the maximum total importance of all roads possible after assigning the
// values optimally.

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  virtual long long maximumImportance(int n,
                                      std::vector<std::vector<int>> &roads) = 0;
};

class Solution1 : public Solution {
public:
  long long maximumImportance(int n, std::vector<std::vector<int>> &roads) {
    std::vector<int> count(n, 0);
    long long ans = 0;

    for (auto r : roads) {
      count[r[0]]++;
      count[r[1]]++;
    }

    std::sort(count.begin(), count.end());

    for (int i = 0; i < n; i++) {
      ans += count[i] * (i + 1);
    }

    return ans;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  int n = 5;
  std::vector<std::vector<int>> roads = {{0, 1}, {1, 2}, {2, 3},
                                         {0, 2}, {1, 3}, {2, 4}};
  int ans = 43;
  int res = sol->maximumImportance(n, roads);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: The figure above shows the country and the assigned values of
  // {2,4,5,3,1}.
  // - The road (0,1) has an importance of 2 + 4 = 6.
  // - The road (1,2) has an importance of 4 + 5 = 9.
  // - The road (2,3) has an importance of 5 + 3 = 8.
  // - The road (0,2) has an importance of 2 + 5 = 7.
  // - The road (1,3) has an importance of 4 + 3 = 7.
  // - The road (2,4) has an importance of 5 + 1 = 6.
  // The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
  // It can be shown that we cannot obtain a greater total importance than 43.

  // Example 2:
  n = 5;
  roads = {{0, 3}, {2, 4}, {1, 3}};
  ans = 20;
  res = sol->maximumImportance(n, roads);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: The figure above shows the country and the assigned values of
  // {4,3,2,5,1}.
  // - The road (0,3) has an importance of 4 + 5 = 9.
  // - The road (2,4) has an importance of 2 + 1 = 3.
  // - The road (1,3) has an importance of 3 + 5 = 8.
  // The total importance of all roads is 9 + 3 + 8 = 20.
  // It can be shown that we cannot obtain a greater total importance than 20.

  // Constraints:
  // 2 <= n <= 5 * 104
  // 1 <= roads.length <= 5 * 104
  // roads[i].length == 2
  // 0 <= ai, bi <= n - 1
  // ai != bi
  // There are no duplicate roads.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
