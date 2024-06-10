// 1051. Height Checker
// Easy
// A school is trying to take an annual photo of all the students. The students
// are asked to stand in a single file line in non-decreasing order by height.
// Let this ordering be represented by the integer array expected where
// expected[i] is the expected height of the ith student in line.

// You are given an integer array heights representing the current order that
// the students are standing in. Each heights[i] is the height of the ith
// student in line (0-indexed).

// Return the number of indices where heights[i] != expected[i].

#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

class Solution {
public:
  virtual int heightChecker(std::vector<int> &heights) = 0;
};

class Solution1 : public Solution {
public:
  virtual int heightChecker(std::vector<int> &heights) {
    int ans = 0;
    std::vector<int> sorted = heights;
    std::sort(sorted.begin(), sorted.end());

    for (int i = 0; i < heights.size(); i++) {
      if (heights[i] != sorted[i]) {
        ans++;
      }
    }
    return ans;
  };
};

class Solution2 : public Solution {
public:
  virtual int heightChecker(std::vector<int> &heights) {
    std::map<int, int> sorted;
    int ans = 0;

    for (int n : heights) {
      sorted[n]++;
    }

    for (int i = 0; i < heights.size(); i++) {
      auto s_it = sorted.begin();
      int first = s_it->first;
      if (heights[i] != first) {
        ans++;
      }
      sorted[first]--;
      if (sorted[first] == 0) {
        sorted.erase(first);
      }
    }
    return ans;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<int> heights = {1, 1, 4, 2, 1, 3};
  int ans = 3;
  int res = sol->heightChecker(heights);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation:
  // heights:  {1,1,4,2,1,3}
  // expected: {1,1,1,2,3,4}
  // Indices 2, 4, and 5 do not match.

  // Example 2:
  heights = {5, 1, 2, 3, 4};
  ans = 5;
  res = sol->heightChecker(heights);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation:
  // heights:  {5,1,2,3,4}
  // expected: {1,2,3,4,5}
  // All indices do not match.

  // Example 3:
  heights = {1, 2, 3, 4, 5};
  ans = 0;
  res = sol->heightChecker(heights);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation:
  // heights:  {1,2,3,4,5}
  // expected: {1,2,3,4,5}
  // All indices match.

  // Constraints:
  // 1 <= heights.length <= 100
  // 1 <= heights{i} <= 100
}

int main() {
  std::cout << "Test 1" << "\n";
  Solution1 sol1;
  test_solution(&sol1);
  std::cout << "Test 2" << "\n";
  Solution2 sol2;
  test_solution(&sol2);
}
