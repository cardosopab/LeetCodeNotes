// 2486. Append Characters to String to Make Subsequence
// Medium
// You are given two strings s and t consisting of only lowercase English
// letters.

// Return the minimum number of characters that need to be appended to the end
// of s so that t becomes a subsequence of s.

// A subsequence is a string that can be derived from another string by deleting
// some or no characters without changing the order of the remaining characters.

#include <iostream>

class Solution {
public:
  virtual int appendCharacters(std::string s, std::string t) = 0;
};

class Solution1 : public Solution {
public:
  int appendCharacters(std::string s, std::string t) {
    int i = 0, j = 0;
    while (i < s.size() && j < t.size()) {
      if (s[i] == t[j]) {
        j++;
      }
      i++;
    }
    return t.size() - j;
  };
};

class Solution2 : public Solution {
public:
  int appendCharacters(std::string s, std::string t) {
    int j = 0;

    for (int i = 0; i < s.size(); i++) {
      j += s[i] == t[j];
    }
    return t.size() - j;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::string s = "coaching";
  std::string t = "coding";
  int ans = 4;
  int res = sol->appendCharacters(s, t);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation: Append the characters "ding" to the end of s so that s =
  // "coachingding". Now, t is a subsequence of s ("coachingding"). It can be
  // shown that appending any 3 characters to the end of s will never make t a
  // subsequence.

  // Example 2:
  s = "abcde";
  t = "a";
  ans = 0;
  res = sol->appendCharacters(s, t);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation: t is already a subsequence of s ("abcde").

  // Example 3:
  s = "z";
  t = "abcde";
  ans = 5;
  res = sol->appendCharacters(s, t);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation: Append the characters "abcde" to the end of s so that s =
  // "zabcde". Now, t is a subsequence of s ("zabcde"). It can be shown that
  // appending any 4 characters to the end of s will never make t a subsequence.

  // Constraints:
  // 1 <= s.length, t.length <= 105
  // s and t consist only of lowercase English letters.
}

int main() {
  std::cout << "Test 1" << std::endl;
  Solution1 sol1;
  test_solution(&sol1);
  std::cout << "Test 2" << std::endl;
  Solution2 sol2;
  test_solution(&sol2);
}
