// 2370. Longest Ideal Subsequence
// Medium
// You are given a string s consisting of lowercase letters and an integer k. We
// call a string t ideal if the following conditions are satisfied: t is a
// subsequence of the string s. The absolute difference in the alphabet order of
// every two adjacent letters in t is less than or equal to k. Return the length
// of the longest ideal string. A subsequence is a string that can be derived
// from another string by deleting some or no characters without changing the
// order of the remaining characters. Note that the alphabet order is not
// cyclic. For example, the absolute difference in the alphabet order of 'a' and
// 'z' is 25, not 1.

#include <algorithm>
#include <array>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  int longestIdealString(string s, int k) {
    array<int, 26> dp = {0};
    int orda = static_cast<int>('a');
    int best = 0;

    for (auto c : s) {
      int ordc = static_cast<int>(c) - orda;
      int length = 1;

      int start = max(0, ordc - k - 1);
      int end = min(26, ordc + k + 1);

      for (int i = start; i < end; i++) {
        if (abs(ordc - i) <= k) {
          length = max(length, 1 + dp[i]);
        }
      }
      best = max(best, length);
      dp[ordc] = length;
    }

    return best;
  }
};

class Solution1 {
public:
  int longestIdealString(string s, int k) {
    unordered_map<int, int> dp;
    int orda = static_cast<int>('a');
    int best = 0;

    for (auto c : s) {
      int ordc = static_cast<int>(c) - orda;
      int length = 1;

      int start = max(0, ordc - k - 1);
      int end = min(26, ordc + k + 1);

      for (int i = start; i < end; i++) {
        bool exists = dp.find(i) != dp.end();
        if (exists && abs(ordc - i) <= k) {
          length = max(length, 1 + dp[i]);
        }
      }

      best = max(best, length);
      dp[ordc] = length;
    }

    return best;
  }
};

template <typename SolutionType> void testLongestIdealString() {
  SolutionType sol;

  // Example 1
  string s1 = "acfgbd";
  int k1 = 2;
  int ans1 = 4;
  int result1 = sol.longestIdealString(s1, k1);
  cout << "Example 1: " << (result1 == ans1 ? "Pass" : "Fail") << " " << result1
       << endl;
  // Explanation: The longest ideal string is "acbd". The length of this string
  // is 4, so 4 is returned.
  // Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3
  // in alphabet order.

  // Example 2:
  string s2 = "abcd";
  int k2 = 3;
  int ans2 = 4;
  int result2 = sol.longestIdealString(s2, k2);
  cout << "Example 2: " << (result2 == ans2 ? "Pass" : "Fail") << " " << result2
       << endl;
  // Explanation: The longest ideal string is "abcd". The length of this string
  // is 4, so 4 is returned.

  // Example 3:
  string s3 = "abcd";
  int k3 = 3;
  int ans3 = 4;
  int result3 = sol.longestIdealString(s3, k3);
  cout << "Example 3: " << (result3 == ans3 ? "Pass" : "Fail") << " " << result3
       << endl;

  // Example 4:
  string s4 = "azaza";
  int k4 = 25;
  int ans4 = 5;
  int result4 = sol.longestIdealString(s4, k4);
  cout << "Example 4: " << (result4 == ans4 ? "Pass" : "Fail") << " " << result4
       << endl;

  // Example 5:
  string s5 = "lopjigzbaq";
  int k5 = 5;
  int ans5 = 7;
  int result5 = sol.longestIdealString(s5, k5);
  cout << "Example 5: " << (result5 == ans5 ? "Pass" : "Fail") << " " << result5
       << endl;

  // Example 6:
  string s6 = "fqyokqgzvjpermqmwcjqtzbxnurjmawsswlwzmnjbbhdtfjxnktwtonpeorewc";
  int k6 = 3;
  int ans6 = 19;
  int result6 = sol.longestIdealString(s6, k6);
  cout << "Example 6: " << (result6 == ans6 ? "Pass" : "Fail") << " " << result6
       << endl;
}

int main() {
  cout << "Test 0:" << endl;
  testLongestIdealString<Solution>();
  cout << "Test 1:" << endl;
  testLongestIdealString<Solution1>();
  return 0;
}