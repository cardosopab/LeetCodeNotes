// 409. Longest Palindrome
// Easy
// Given a string s which consists of lowercase or uppercase letters, return the
// length of the longest palindrome that can be built with those letters.

// Letters are case sensitive, for example, "Aa" is not considered a palindrome.

#include <iostream>
#include <unordered_set>

class Solution {
public:
  virtual int longestPalindrome(std::string s) = 0;
};

class Solution1 : public Solution {
public:
  int longestPalindrome(std::string s) {
    std::unordered_set<int> search;
    int ans = 0;
    for (auto c : s) {
      if (search.find(c) == search.end()) {
        search.insert(c);
      } else {
        search.erase(c);
        ans += 2;
      }
    }
    if (search.size() > 0) {
      ans++;
    }
    return ans;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::string s = "abccccdd";
  int ans = 7;
  int res = sol->longestPalindrome(s);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation: One longest palindrome that can be built is "dccaccd", whose
  // length is 7.

  // Example 2:
  s = "a";
  ans = 1;
  res = sol->longestPalindrome(s);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation: The longest palindrome that can be built is "a", whose length
  // is 1.

  // Constraints:
  // 1 <= s.length <= 2000
  // s consists of lowercase and/or uppercase English letters only.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
