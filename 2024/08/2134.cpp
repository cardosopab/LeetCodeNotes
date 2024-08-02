// 2134. Minimum Swaps to Group All 1's Together II
// Attempted
// Medium
// Topics
// Companies
// Hint
// A swap is defined as taking two distinct positions in an array and swapping
// the values in them.

// A circular array is defined as an array where we consider the first element
// and the last element to be adjacent.

// Given a binary circular array nums, return the minimum number of swaps
// required to group all 1's present in the array together at any location.

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  virtual int minSwaps(std::vector<int> &nums) = 0;
};

class Solution1 : public Solution {
public:
  int minSwaps(std::vector<int> &nums) {
    int total_ones =
        std::count_if(nums.begin(), nums.end(), [](auto n) { return n; });
    int l = 0, window_ones = 0, max_window_ones = 0, N = nums.size();

    for (int r = 0; r < N * 2; r++) {
      if (nums[r % N]) {
        window_ones++;
      }
      if (r - l + 1 > total_ones) {
        window_ones -= nums[l % N];
        l++;
      }
      max_window_ones = std::max(max_window_ones, window_ones);
    }

    return total_ones - max_window_ones;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<int> nums = {0, 1, 0, 1, 1, 0, 0};
  int ans = 1;
  int res = sol->minSwaps(nums);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: Here are a few of the ways to group all the 1's together:
  // {0,0,1,1,1,0,0} using 1 swap.
  // {0,1,1,1,0,0,0} using 1 swap.
  // {1,1,0,0,0,0,1} using 2 swaps (using the circular property of the array).
  // There is no way to group all 1's together with 0 swaps.
  // Thus, the minimum number of swaps required is 1.

  // Example 2:
  nums = {0, 1, 1, 1, 0, 0, 1, 1, 0};
  ans = 2;
  res = sol->minSwaps(nums);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: Here are a few of the ways to group all the 1's together:
  // {1,1,1,0,0,0,0,1,1} using 2 swaps (using the circular property of the
  // array). {1,1,1,1,1,0,0,0,0} using 2 swaps. There is no way to group all
  // 1's together with 0 or 1 swaps. Thus, the minimum number of swaps
  // required is 2.

  // Example 3:
  nums = {1, 1, 0, 0, 1};
  ans = 0;
  res = sol->minSwaps(nums);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: All the 1's are already grouped together due to the circular
  // property of the array. Thus, the minimum number of swaps required is 0.

  // Constraints:
  // 1 <= nums.length <= 105
  // nums[i] is either 0 or 1.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
