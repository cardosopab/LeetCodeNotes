// 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to
// Limit Medium Given an array of integers nums and an integer limit, return the
// size of the longest non-empty subarray such that the absolute difference
// between any two elements of this subarray is less than or equal to limit.

#include <deque>
#include <iostream>
#include <vector>

class Solution {
public:
  virtual int longestSubarray(std::vector<int> &nums, int limit) = 0;
};

class Solution1 : public Solution {
public:
  int longestSubarray(std::vector<int> &nums, int limit) {
    std::deque<int> max_q;
    std::deque<int> min_q;
    int left = 0, ans = 0, N = nums.size(), n;

    for (int right = 0; right < N; right++) {
      n = nums[right];
      while (!max_q.empty() && max_q.back() < n) {
        max_q.pop_back();
      }
      max_q.push_back(n);

      while (!min_q.empty() && min_q.back() > n) {
        min_q.pop_back();
      }
      min_q.push_back(n);

      while (max_q.front() - min_q.front() > limit) {
        n = nums[left++];
        if (max_q.front() == n) {
          max_q.pop_front();
        }
        if (min_q.front() == n) {
          min_q.pop_front();
        }
      }
      ans = std::max(ans, right - left + 1);
    }
    return ans;
  };
};

void solution_test(Solution *sol) {
  // Example 1:
  std::vector<int> nums = {8, 2, 4, 7};
  int limit = 4;
  int ans = 2;
  int res = sol->longestSubarray(nums, limit);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: All subarrays are:
  // {8} with maximum absolute diff |8-8| = 0 <= 4.
  // {8,2} with maximum absolute diff |8-2| = 6 > 4.
  // {8,2,4} with maximum absolute diff |8-2| = 6 > 4.
  // {8,2,4,7} with maximum absolute diff |8-2| = 6 > 4.
  // {2} with maximum absolute diff |2-2| = 0 <= 4.
  // {2,4} with maximum absolute diff |2-4| = 2 <= 4.
  // {2,4,7} with maximum absolute diff |2-7| = 5 > 4.
  // {4} with maximum absolute diff |4-4| = 0 <= 4.
  // {4,7} with maximum absolute diff |4-7| = 3 <= 4.
  // {7} with maximum absolute diff |7-7| = 0 <= 4.
  // Therefore, the size of the longest subarray is 2.

  // Example 2:
  nums = {10, 1, 2, 4, 7, 2};
  limit = 5;
  ans = 4;
  res = sol->longestSubarray(nums, limit);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The subarray {2,4,7,2} is the longest since the maximum
  // absolute diff is |2-7| = 5 <= 5.

  // Example 3:
  nums = {4, 2, 2, 2, 4, 4, 2, 2};
  limit = 0;
  ans = 3;
  res = sol->longestSubarray(nums, limit);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';

  // Constraints:
  // 1 <= nums.length <= 105
  // 1 <= nums{i} <= 109
  // 0 <= limit <= 109
}

int main() {
  Solution1 sol1;
  solution_test(&sol1);
}
