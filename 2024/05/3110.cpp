// 3110. Score of a String
// Easy
// You are given a string s. The score of a string is defined as the sum of the
// absolute difference between the ASCII values of adjacent characters.
//
// Return the score of s.

#include <cstdlib>
#include <iostream>

class Solution {
public:
  virtual int scoreOfString(std::string s) = 0;
};

class Solution1 : public Solution {
public:
  int scoreOfString(std::string s) {
    int ans = 0;
    for (int i = 1; i < s.size(); i++) {
      ans += abs(int(s[i]) - int(s[i - 1]));
    }
    return ans;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::string s1 = "hello";
  int ans1 = 13;
  int res1 = sol->scoreOfString(s1);
  std::cout << (ans1 == res1 ? "Pass" : "Fail") << std::endl;
  // Explanation:
  // The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' =
  // 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| +
  // |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
  //
  // Example 2:
  std::string s2 = "zaz";
  int ans2 = 50;
  int res2 = sol->scoreOfString(s2);
  std::cout << (ans2 == res2 ? "Pass" : "Fail") << std::endl;
  // Explanation:
  // The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the
  // score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
  //
  // Constraints:
  // 2 <= s.length <= 100
  // s consists only of lowercase English letters.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
  return 0;
}
