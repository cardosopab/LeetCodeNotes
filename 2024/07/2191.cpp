// 2191. Sort the Jumbled Numbers
// Medium
// You are given a 0-indexed integer array mapping which represents the mapping
// rule of a shuffled decimal system. mapping[i] = j means digit i should be
// mapped to digit j in this system.

// The mapped value of an integer is the new integer obtained by replacing each
// occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

// You are also given another integer array nums. Return the array nums sorted
// in non-decreasing order based on the mapped values of its elements.

// Notes:
// Elements with the same mapped values should appear in the same relative order
// as in the input. The elements of nums should only be sorted based on their
// mapped values and not be replaced by them.

#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
class Solution {
public:
  virtual std::vector<int> sortJumbled(std::vector<int> &mapping,
                                       std::vector<int> &nums) = 0;
};

class Solution1 : public Solution {
public:
  std::vector<int> sortJumbled(std::vector<int> &mapping,
                               std::vector<int> &nums) {
    std::vector<int> ans;
    std::vector<std::pair<int, int>> pairs(nums.size());

    // add mapped n and i to pairs
    for (int i = 0; i < nums.size(); i++) {
      int m = 0, n = nums[i], place = 1;
      if (n == 0) {
        m = mapping[n];
      }
      while (n) {
        m += mapping[(n % 10)] * place;
        n /= 10;
        place *= 10;
      }
      pairs[i] = {m, i};
    }

    // sort
    std::sort(pairs.begin(), pairs.end());

    // return ans
    for (const auto &[_, i] : pairs) {
      ans.push_back(nums[i]);
    }

    return ans;
  }
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<int> mapping = {8, 9, 4, 0, 2, 1, 3, 5, 7, 6};
  std::vector<int> nums = {991, 338, 38};
  std::vector<int> ans = {338, 38, 991};
  std::vector<int> res = sol->sortJumbled(mapping, nums);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';

  // Explanation:
  // Map the number 991 as follows:
  // 1. mapping{9} = 6, so all occurrences of the digit 9 will become 6.
  // 2. mapping{1} = 9, so all occurrences of the digit 1 will become 9.
  // Therefore, the mapped value of 991 is 669.
  // 338 maps to 007, or 7 after removing the leading zeros.
  // 38 maps to 07, which is also 7 after removing leading zeros.
  // Since 338 and 38 share the same mapped value, they should remain in the
  // same relative order, so 338 comes before 38. Thus, the sorted array is
  // {338,38,991}.

  // Example 2:
  mapping = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  nums = {789, 456, 123};
  ans = {123, 456, 789};
  res = sol->sortJumbled(mapping, nums);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';

  // Explanation: 789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus,
  // the sorted array is [123,456,789].

  // Constraints:
  // mapping.length == 10
  // 0 <= mapping[i] <= 9
  // All the values of mapping[i] are unique.
  // 1 <= nums.length <= 3 * 104
  // 0 <= nums[i] < 109
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
