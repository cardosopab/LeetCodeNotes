// 1508. Range Sum of Sorted Subarray Sums
// Medium
// You are given the array nums consisting of n positive integers. You computed
// the sum of all non-empty continuous subarrays from the array and then sorted
// them in non-decreasing order, creating a new array of n * (n + 1) / 2
// numbers.

// Return the sum of the numbers from index left to index right (indexed from
// 1), inclusive, in the new array. Since the answer can be a huge number return
// it modulo 109 + 7.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

class Solution
{
public:
  virtual int rangeSum(std::vector<int> &nums, int n, int left, int right) = 0;
};

class Solution1 : public Solution
{
public:
  int rangeSum(std::vector<int> &nums, int n, int left, int right)
  {
    int MOD = 1000000007;
    intmax_t ans = 0;
    std::vector<int> range;

    for (int i = 0; i < n; i++)
    {
      int curr = 0;
      for (int j = i; j < n; j++)
      {
        curr += nums[j];
        range.push_back(curr);
      }
    }

    std::sort(range.begin(), range.end());
    for (int i = left - 1; i < right; i++)
    {
      ans += range[i];
    }
    return ans % MOD;
  }
};

void test_solution(Solution *sol)
{
  // Example 1:
  std::vector<int> nums = {1, 2, 3, 4};
  int n = 4;
  int left = 1;
  int right = 5;
  int ans = 13;
  int res = sol->rangeSum(nums, n, left, right);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After
  // sorting them in non-decreasing order we have the new array {1, 2, 3, 3, 4,
  // 5, 6, 7, 9, 10}. The sum of the numbers from index le = 1 to ri = 5 is 1 +
  // 2 + 3 + 3 + 4 = 13.

  // Example 2:
  nums = {1, 2, 3, 4};
  n = 4;
  left = 3;
  right = 4;
  ans = 6;
  res = sol->rangeSum(nums, n, left, right);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The given array is the same as example 1. We have the new
  // array {1, 2, 3, 3, 4, 5, 6, 7, 9, 10}. The sum of the numbers from index le
  // = 3 to ri = 4 is 3 + 3 = 6.

  // Example 3:
  nums = {1, 2, 3, 4};
  n = 4;
  left = 1;
  right = 10;
  ans = 50;
  res = sol->rangeSum(nums, n, left, right);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';

  // Constraints:
  // n == nums.length
  // 1 <= nums.length <= 1000
  // 1 <= nums[i] <= 100
  // 1 <= left <= right <= n * (n + 1) / 2
}

int main()
{
  Solution1 sol1;
  test_solution(&sol1);
}
