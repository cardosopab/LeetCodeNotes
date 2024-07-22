// 2418. Sort the People
// Easy
// You are given an array of strings names, and an array heights that consists
// of distinct positive integers. Both arrays are of length n.

// For each index i, names[i] and heights[i] denote the name and height of the
// ith person.

// Return names sorted in descending order by the people's heights.

#include <algorithm>
#include <iostream>
#include <iterator>
#include <map>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
  virtual std::vector<std::string> sortPeople(std::vector<std::string> &names,
                                              std::vector<int> &heights) = 0;
};

class Solution1 : public Solution {
public:
  std::vector<std::string> sortPeople(std::vector<std::string> &names,
                                      std::vector<int> &heights) {
    std::map<int, std::string> h_to_n;
    std::vector<std::string> ans;
    ans.reserve(names.size());

    std::transform(
        heights.begin(), heights.end(), names.begin(),
        std::inserter(h_to_n, h_to_n.end()),
        [](const int &h, const auto &n) { return std::make_pair(h, n); });

    for (auto it = h_to_n.rbegin(); it != h_to_n.rend(); it++) {
      ans.push_back(it->second);
    }

    return ans;
  };
};

class Solution2 : public Solution {
public:
  std::vector<std::string> sortPeople(std::vector<std::string> &names,
                                      std::vector<int> &heights) {
    std::vector<std::pair<int, std::string>> order;
    std::vector<std::string> ans;
    int N = names.size();
    ans.reserve(N);
    order.reserve(N);

    for (int i = 0; i < N; i++) {
      order.push_back({heights[i], names[i]});
    }

    std::sort(order.begin(), order.end());

    for (int i = N - 1; i >= 0; i--) {
      ans.push_back(order[i].second);
    }

    return ans;
  };
};

class Solution3 : public Solution {
public:
  std::vector<std::string> sortPeople(std::vector<std::string> &names,
                                      std::vector<int> &heights) {
    std::vector<std::pair<int, std::string>> order;
    std::vector<std::string> ans;
    int N = names.size();
    ans.reserve(N);
    order.reserve(N);

    for (int i = 0; i < N; i++) {
      order.push_back({heights[i], names[i]});
    }

    std::sort(order.rbegin(), order.rend());

    for (auto [_, n] : order) {
      ans.push_back(n);
    }

    return ans;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<std::string> names = {"Mary", "John", "Emma"};
  std::vector<int> heights = {180, 165, 170};
  std::vector<std::string> ans = {"Mary", "Emma", "John"};
  std::vector<std::string> res = sol->sortPeople(names, heights);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: Mary is the tallest, followed by Emma and John.

  // Example 2:
  names = {"Alice", "Bob", "Bob"};
  heights = {155, 185, 150};
  ans = {"Bob", "Alice", "Bob"};
  res = sol->sortPeople(names, heights);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The first Bob is the tallest, followed by Alice and the
  // second Bob.

  // Constraints:
  // n == names.length == heights.length
  // 1 <= n <= 103
  // 1 <= names[i].length <= 20
  // 1 <= heights[i] <= 105
  // names[i] consists of lower and upper case English letters.
  // All the values of heights are distinct.
}

int main() {
  std::cout << "Test 1" << '\n';
  Solution1 sol1;
  test_solution(&sol1);
  std::cout << "Test 2" << '\n';
  Solution2 sol2;
  test_solution(&sol2);
  std::cout << "Test 3" << '\n';
  Solution3 sol3;
  test_solution(&sol3);
}
