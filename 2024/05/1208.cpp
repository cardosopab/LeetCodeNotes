// 1208. Get Equal Substrings Within Budget
// Medium
// You are given two strings s and t of the same length and an integer maxCost.

// You want to change s to t. Changing the ith character of s to ith character
// of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII
// values of the characters).

// Return the maximum length of a substring of s that can be changed to be the
// same as the corresponding substring of t with a cost less than or equal to
// maxCost. If there is no substring from s that can be changed to its
// corresponding substring from t, return 0.

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <ostream>

class Solution {
public:
  virtual int equalSubstring(std::string s, std::string t, int maxCost) = 0;
};

class Solution1 : public Solution {
public:
  virtual int equalSubstring(std::string s, std::string t, int maxCost) {
    int best = 0;
    int left = 0;
    int curr = 0;
    int N = s.size();

    for (int right = 0; right < N; right++) {
      curr += std::abs(int(s[right]) - int(t[right]));
      while (curr > maxCost) {
        curr -= std::abs(int(s[left]) - int(t[left]));
        left++;
      }
      best = std::max(best, right - left + 1);
    }
    return best;
  };
};

void test_solution(Solution &sol) {
  // Example 1:
  std::string s1 = "abcd";
  std::string t1 = "bcdf";
  int maxCost1 = 3;
  int res1 = sol.equalSubstring(s1, t1, maxCost1);
  int ans1 = 3;
  std::cout << (res1 == ans1 ? "Pass" : "Fail") << std::endl;
  // Explanation: "abc" of s can change to "bcd".
  // That costs 3, so the maximum length is 3.

  // Example 2:
  std::string s2 = "abcd";
  std::string t2 = "cdef";
  int maxCost2 = 3;
  int res2 = sol.equalSubstring(s2, t2, maxCost2);
  int ans2 = 1;
  std::cout << (res2 == ans2 ? "Pass" : "Fail") << std::endl;
  // Explanation: Each character in s costs 2 to change to character in t,  so
  // the maximum length is 1.

  // Example 3:
  std::string s3 = "abcd";
  std::string t3 = "acde";
  int maxCost3 = 0;
  int res3 = sol.equalSubstring(s3, t3, maxCost3);
  int ans3 = 1;
  std::cout << (res3 == ans3 ? "Pass" : "Fail") << std::endl;
  // Explanation: You cannot make any change, so the maximum length is 1.

  // Constraints:
  // 1 <= s.length <= 105
  // t.length == s.length
  // 0 <= maxCost <= 106
  // s and t consist of only lowercase English letters.
}

int main() {
  Solution1 sol1;
  test_solution(sol1);
  return 0;
}
