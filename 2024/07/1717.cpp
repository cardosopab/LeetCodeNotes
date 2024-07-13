// 1717. Maximum Score From Removing Substrings
// Medium
// You are given a string s and two integers x and y. You can perform two types
// of operations any number of times.

// Remove substring "ab" and gain x points.
// For example, when removing "ab" from "cabxbae" it becomes "cxbae".
// Remove substring "ba" and gain y points.
// For example, when removing "ba" from "cabxbae" it becomes "cabxe".
// Return the maximum points you can gain after applying the above operations on
// s.

#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
  virtual int maximumGain(std::string s, int x, int y) = 0;
};

class Solution1 : public Solution {
public:
  int maximumGain(std::string s, int x, int y) {
    std::vector<char> first;
    std::vector<char> second;
    int ans = 0;
    char a = x > y ? 'a' : 'b';
    char b = x > y ? 'b' : 'a';

    for (char c : s) {
      if (!first.empty() && first.back() == a && c == b) {
        ans += std::max(x, y);
        first.pop_back();
      } else {
        first.push_back(c);
      }
    }

    while (!first.empty()) {
      char c = first.back();
      first.pop_back();

      if (!second.empty() && second.back() == a && c == b) {
        ans += std::min(x, y);
        second.pop_back();
      }
      second.push_back(c);
    }

    return ans;
  };
};

void test_solution(Solution *sol) {

  // Example 1:
  std::string s = "cdbcbbaaabab";
  int x = 4;
  int y = 5;
  int ans = 19;
  int res = sol->maximumGain(s, x, y);
  std::cout << (ans == res ? "Pass" : "Fail ") << '\n';
  // Explanation:
  // - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5
  // points are added to the score.
  // - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4
  // points are added to the score.
  // - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points
  // are added to the score.
  // - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are
  // added to the score. Total score = 5 + 4 + 5 + 5 = 19.

  // Example 2:
  s = "aabbaaxybbaabb";
  x = 5;
  y = 4;
  ans = 20;
  res = sol->maximumGain(s, x, y);
  std::cout << (ans == res ? "Pass" : "Fail ") << '\n';

  // Constraints:
  // 1 <= s.length <= 105
  // 1 <= x, y <= 104
  // s consists of lowercase English letters.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
