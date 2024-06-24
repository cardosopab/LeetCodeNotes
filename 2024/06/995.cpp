// 995. Minimum Number of K Consecutive Bit Flips
// Hard
// You are given a binary array nums and an integer k.

// A k-bit flip is choosing a subarray of length k from nums and simultaneously
// changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

// Return the minimum number of k-bit flips required so that there is no 0 in
// the array. If it is not possible, return -1.

// A subarray is a contiguous part of an array.

#include <deque>
#include <iostream>
#include <vector>

class Solution {
public:
  virtual int minKBitFlips(std::vector<int> &nums, int k) = 0;
};

class Solution1 : public Solution {
public:
  int minKBitFlips(std::vector<int> &nums, int k) {
    int ans = 0, N = nums.size();
    std::deque<int> flips;

    for (int i = 0; i < N; i++) {
      if (!flips.empty() && flips.front() < i) {
        flips.pop_front();
      }
      int curr = (nums[i] + flips.size()) % 2;
      if (curr == 0) {
        if (i > N - k) {
          return -1;
        };
        ans++;
        flips.push_back(i + k - 1);
      }
    }
    return ans;
  };
};

// Time Limit Exceeded on Leetcode
class Solution2 : public Solution {
public:
  int minKBitFlips(std::vector<int> &nums, int k) {
    int ans = 0, N = nums.size();

    for (int i = 0; i < N; i++) {
      if (nums[i] == 0) {
        if (i + k > N) {
          return -1;
        };
        ans++;
        for (int j = 0; j < k; j++) {
          nums[i + j] ^= 1;
        }
      }
    }
    return ans;
  };
};

void solution_test(Solution *sol) {
  // Example 1:
  std::vector<int> nums = {0, 1, 0};
  int k = 1;
  int ans = 2;
  int res = sol->minKBitFlips(nums, k);
  std::cout << (ans == res ? "Pass" : "Fail") << " : " << res << '\n';
  // Explanation: Flip nums{0}, then flip nums[2}.

  // Example 2:
  nums = {1, 1, 0};
  k = 2;
  ans = -1;
  res = sol->minKBitFlips(nums, k);
  std::cout << (ans == res ? "Pass" : "Fail") << " : " << res << '\n';
  // Explanation: No matter how we flip subarrays of size 2, we cannot make the
  // array become {1,1,1}.

  // Example 3:
  nums = {0, 0, 0, 1, 0, 1, 1, 0};
  k = 3;
  ans = 3;
  res = sol->minKBitFlips(nums, k);
  std::cout << (ans == res ? "Pass" : "Fail") << " : " << res << '\n';
  // Explanation:
  // Flip nums{0},nums[1},nums[2}: nums becomes [1,1,1,1,0,1,1,0}
  // Flip nums{4},nums[5},nums[6}: nums becomes [1,1,1,1,1,0,0,0}
  // Flip nums{5},nums[6},nums[7}: nums becomes [1,1,1,1,1,1,1,1}

  // Constraints:
  // 1 <= nums.length <= 105
  // 1 <= k <= nums.length
}

int main() {
  std::cout << "Solution 1" << '\n';
  Solution1 sol1;
  solution_test(&sol1);

  std::cout << "Solution 2" << '\n';
  Solution2 sol2;
  solution_test(&sol2);
}
