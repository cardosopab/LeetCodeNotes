// 1137. N-th Tribonacci Number
// Easy
// The Tribonacci sequence Tn is defined as follows:
// T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
// Given n, return the value of Tn.

#include <functional>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int tribonacci(int n) {
    vector<bool> has_cache(n + 1, false);
    vector<int> cache(n + 1, 0);

    return calc(n, has_cache, cache);
  }

  int calc(int n, vector<bool> &has_cache, vector<int> &cache) {
    if (n == 0) {
      return 0;
    }
    if (n == 1 || n == 2) {
      return 1;
    }

    if (has_cache[n]) {
      return cache[n];
    }

    has_cache[n] = true;
    cache[n] = calc(n - 1, has_cache, cache) + calc(n - 2, has_cache, cache) +
               calc(n - 3, has_cache, cache);
    return cache[n];
  }
};

class Solution1 {
public:
  int tribonacci(int n) {
    if (n == 0) {
      return 0;
    }
    if (n == 1 || n == 2) {
      return 1;
    }

    vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;

    for (int i = 3; i <= n; i++) {
      dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
    return dp[n];
  }
};

class Solution2 {
public:
  int tribonacci(int n) {
    vector<bool> has_cache(n + 1, false);
    vector<int> cache(n + 1, 0);

    function<int(int)> calc = [&](int n) {
      if (n == 0) {
        return 0;
      }
      if (n == 1 || n == 2) {
        return 1;
      }

      if (has_cache[n]) {
        return cache[n];
      }

      has_cache[n] = true;
      cache[n] = calc(n - 1) + calc(n - 2) + calc(n - 3);
      return cache[n];
    };
    return calc(n);
  }
};

template <typename SolutionType> void testTribonacci() {
  SolutionType sol;

  // Example 1
  int n1 = 4;
  int ans1 = 4;
  int result1 = sol.tribonacci(n1);
  cout << "Example 1: " << (result1 == ans1 ? "Pass" : "Fail") << " " << result1
       << endl;
  // Explanation:
  // T_3 = 0 + 1 + 1 = 2
  // T_4 = 1 + 1 + 2 = 4

  // Example 2:
  // Example 1
  int n2 = 25;
  int ans2 = 1389537;
  int result2 = sol.tribonacci(n2);
  cout << "Example 2: " << (result2 == ans2 ? "Pass" : "Fail") << " " << result2
       << endl;
  // Explanation: There is no path from vertex 0 to vertex 5.

  // Example 3:
  int n3 = 37;
  int ans3 = 2082876103;
  int result3 = sol.tribonacci(n3);
  cout << "Example 3: " << (result3 == ans3 ? "Pass" : "Fail") << " " << result3
       << endl;
}

int main() {
  cout << "Test 0:" << endl;
  testTribonacci<Solution>();
  cout << "Test 1:" << endl;
  testTribonacci<Solution1>();
  cout << "Test 2:" << endl;
  testTribonacci<Solution2>();
  return 0;
}