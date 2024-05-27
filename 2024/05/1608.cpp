// 1608. Special Array With X Elements Greater Than or Equal X
// Easy
// You are given an array nums of non-negative integers. nums is considered
// special if there exists a number x such that there are exactly x numbers in
// nums that are greater than or equal to x.
//
// Notice that x does not have to be an element in nums.
//
// Return x if the array is special, otherwise, return -1. It can be proven that
// if nums is special, the value for x is unique.

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  virtual int specialArray(std::vector<int> &nums) = 0;
};

class Solution1 : public Solution {
public:
  int specialArray(std::vector<int> &nums) {
    int max_n = *std::max_element(nums.begin(), nums.end());

    std::vector<int> bucket(max_n + 1, 0);

    for (int n : nums) {
      bucket[n]++;
    }

    int best = 0;
    for (int i = max_n; i >= 0; i--) {
      best += bucket[i];
      if (best == i) {
        return i;
      }
    }
    return -1;
  };
};

void test_solution(Solution &sol) {
  // Example 1:
  std::vector<int> nums1 = {3, 5};
  int ans1 = 2;
  int res1 = sol.specialArray(nums1);
  std::cout << (res1 == ans1 ? "Pass" : "Fail") << std::endl;
  // Explanation: There are 2 values (3 and 5) that
  // are greater than or equal to 2.

  // Example 2:
  std::vector<int> nums2 = {0, 0};
  int ans2 = -1;
  int res2 = sol.specialArray(nums2);
  std::cout << (res1 == ans1 ? "Pass" : "Fail") << std::endl;
  // Explanation: No numbers fit the criteria for x.
  // If x = 0, there should be 0 numbers >= x, but there are 2.
  // If x = 1, there should be 1 number >= x, but there are 0.
  // If x = 2, there should be 2 numbers >= x, but there are 0.
  // x cannot be greater since there are only 2 numbers in nums.

  // Example 3:
  std::vector<int> nums3 = {0, 4, 3, 0, 4};
  int ans3 = 3;
  int res3 = sol.specialArray(nums3);
  std::cout << (res1 == ans1 ? "Pass" : "Fail") << std::endl;
  // Explanation: There are 3 values that are greater than or equal to 3.

  // Constraints:
  // 1 <= nums.length <= 100
  // 0 <= nums{i} <= 1000
};

int main() {
  Solution1 sol1;
  test_solution(sol1);
  return 0;
}
