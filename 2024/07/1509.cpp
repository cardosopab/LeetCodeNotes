// 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
// Medium
// You are given an integer array nums.

// In one move, you can choose one element of nums and change it to any value.

// Return the minimum difference between the largest and smallest value of nums
// after performing at most three moves.

#include <algorithm>
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <vector>

class Solution {
public:
  virtual int minDifference(std::vector<int> &nums) = 0;
};

class Solution1 : public Solution {
public:
  int minDifference(std::vector<int> &nums) {
    if (nums.size() <= 4) {
      return 0;
    }
    std::priority_queue<int> max_heap;
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    int ans = std::numeric_limits<int>::max();

    for (int n : nums) {
      max_heap.push(n);
      min_heap.push(n);
    };

    int n_max[4];
    int n_min[4];

    for (int i = 0; i < 4; i++) {
      int max_curr = max_heap.top();
      max_heap.pop();
      n_max[i] = max_curr;

      int min_curr = min_heap.top();
      min_heap.pop();
      n_min[3 - i] = min_curr;
    }

    for (int i = 0; i < 4; i++) {
      ans = std::min(ans, (n_max[i] - n_min[i]));
    }
    return ans;
  };
};

class Solution2 : public Solution {
public:
  int minDifference(std::vector<int> &nums) {
    if (nums.size() <= 4) {
      return 0;
    }

    std::sort(nums.begin(), nums.end());
    int ans = std::numeric_limits<int>::max(), N = nums.size();

    for (int i = 0; i < 3; i++) {
      int right = nums[N - 4 + i];
      ans = std::min(ans, (right - nums[i]));
    }
    return ans;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<int> nums = {5, 3, 2, 4};
  int ans = 0;
  int res = sol->minDifference(nums);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: We can make at most 3 moves.
  // In the first move, change 2 to 3. nums becomes {5,3,3,4}.
  // In the second move, change 4 to 3. nums becomes {5,3,3,3}.
  // In the third move, change 5 to 3. nums becomes {3,3,3,3}.
  // After performing 3 moves, the difference between the minimum and
  // maximum is
  // 3
  // - 3 = 0.

  // Example 2:
  nums = {1, 5, 0, 10, 14};
  ans = 1;
  res = sol->minDifference(nums);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: We can make at most 3 moves.
  // In the first move, change 5 to 0. nums becomes {1,0,0,10,14}.
  // In the second move, change 10 to 0. nums becomes {1,0,0,0,14}.
  // In the third move, change 14 to 1. nums becomes {1,0,0,0,1}.
  // After performing 3 moves, the difference between the minimum and
  // maximum is
  // 1
  // - 0 = 1. It can be shown that there is no way to make the difference 0
  // in 3 moves.

  // Example 3:
  nums = {3, 100, 20};
  ans = 0;
  res = sol->minDifference(nums);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: We can make at most 3 moves.
  // In the first move, change 100 to 7. nums becomes [3,7,20].
  // In the second move, change 20 to 7. nums becomes [3,7,7].
  // In the third move, change 3 to 7. nums becomes [7,7,7].
  // After performing 3 moves, the difference between the minimum and maximum is
  // 7
  // - 7 = 0.

  // Constraints:
  // 1 <= nums.length <= 105
  // -109 <= nums[i] <= 109
}

int main() {
  std::cout << "Test 1" << '\n';
  Solution1 sol1;
  test_solution(&sol1);

  std::cout << "Test 2" << '\n';
  Solution2 sol2;
  test_solution(&sol2);
}
