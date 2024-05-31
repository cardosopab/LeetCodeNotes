// 260. Single Number III
// Medium
// Given an integer array nums, in which exactly two elements appear only once
// and all the other elements appear exactly twice. Find the two elements that
// appear only once. You can return the answer in any order.

// You must write an algorithm that runs in linear runtime complexity and uses
// only constant extra space.

#include <iostream>
#include <vector>
class Solution {
public:
  virtual std::vector<int> singleNumber(std::vector<int> &nums) = 0;
};

class Solution1 : public Solution {
public:
  std::vector<int> singleNumber(std::vector<int> &nums) {
    int x = 0;
    for (int n : nums) {
      x ^= n;
    }

    int bit = 0;
    for (int i = 0; i < 32; i++) {
      if (((1 << i) & x) != 0) {
        bit = 1 << i;
        break;
      }
    }

    int first = 0;
    for (int n : nums) {
      if ((n & bit) != 0) {
        first ^= n;
      }
    }

    int second = x ^ first;

    return {first, second};
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<int> nums1 = {1, 2, 1, 3, 2, 5};
  std::vector<int> ans1 = {3, 5};
  std::vector<int> res1 = sol->singleNumber(nums1);
  std::cout << (ans1 == res1 ? "Pass" : "Fail") << std::endl;
  // Explanation:  {5, 3} is also a valid answer.

  // Example 2:
  std::vector<int> nums2 = {-1, 0};
  std::vector<int> ans2 = {-1, 0};
  std::vector<int> res2 = sol->singleNumber(nums2);
  std::cout << (ans2 == res2 ? "Pass" : "Fail") << std::endl;

  // Example 3:
  std::vector<int> nums3 = {0, 1};
  std::vector<int> ans3 = {1, 0};
  std::vector<int> res3 = sol->singleNumber(nums3);
  std::cout << (ans3 == res3 ? "Pass" : "Fail") << std::endl;

  // Constraints:
  // 2 <= nums.length <= 3 * 104
  // -231 <= nums[i] <= 231 - 1
  // Each integer in nums will appear twice, only two integers will appear once.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
  return 0;
}
