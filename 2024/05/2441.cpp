// 2441. Largest Positive Integer That Exists With Its Negative
// Easy
// Given an integer array nums that does not contain any zeros, find the largest
// positive integer k such that -k also exists in the array.

// Return the positive integer k. If there is no such integer, return -1.

#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
  virtual int findMaxK(vector<int> &nums) = 0;
};
class Solution1 : public Solution {
public:
  int findMaxK(vector<int> &nums) {
    unordered_set<int> cache;
    int ans = -1;

    for (int n : nums) {
      if (cache.count(-n) == 1) {
        ans = max(ans, abs(n));
      }
      cache.insert(n);
    }
    return ans;
  }
};

class Solution2 : public Solution {
public:
  int findMaxK(vector<int> &nums) {
    sort(nums.begin(), nums.end());

    int left = 0;
    int right = nums.size() - 1;

    while (left < right && nums[left] < 0 && nums[right] > 0) {
      if (abs(nums[left]) == nums[right]) {
        return nums[right];
      }
      if (abs(nums[left]) > nums[right]) {
        left++;
      } else {
        right--;
      }
    }
    return -1;
  }
};

void test_solution(Solution &sol) {
  // Example 1:
  vector<int> nums1 = {-1, 2, -3, 3};
  int ans1 = 3;
  int res1 = sol.findMaxK(nums1);
  cout << "Test 1" << ": " << res1 << " " << (res1 == ans1 ? "Pass" : "Fail")
       << endl;
  // Explanation: 3 is the only valid k we can find in the array.

  // Example 2:
  vector<int> nums2 = {-1, 10, 6, 7, -7, 1};
  int ans2 = 7;
  int res2 = sol.findMaxK(nums2);
  cout << "Test 2" << ": " << res2 << " " << (res2 == ans2 ? "Pass" : "Fail")
       << endl;
  // Explanation: Both 1 and 7 have their corresponding negative values in the
  // array. 7 has a larger value.

  // Example 3:
  vector<int> nums3 = {-10, 8, 6, 7, -2, -3};
  int ans3 = -1;
  int res3 = sol.findMaxK(nums3);
  cout << "Test 3" << ": " << res3 << " " << (res3 == ans3 ? "Pass" : "Fail")
       << endl;
  // Explanation: There is no a single valid k, we return -1.

  // Example 4:
  vector<int> nums4 = {100, 100};
  int ans4 = -1;
  int res4 = sol.findMaxK(nums4);
  cout << "Test 4" << ": " << res4 << " " << (res4 == ans4 ? "Pass" : "Fail")
       << endl;

  // Example 5:
  vector<int> nums5 = {-100, -100};
  int ans5 = -1;
  int res5 = sol.findMaxK(nums5);
  cout << "Test 5" << ": " << res5 << " " << (res5 == ans5 ? "Pass" : "Fail")
       << endl;

  // Constraints:
  // 1 <= nums.length <= 1000
  // -1000 <= nums[i] <= 1000
  // nums[i] != 0
}

int main() {
  Solution1 sol1;
  Solution2 sol2;
  cout << "Testing Solution1:" << endl;
  test_solution(sol1);
  cout << "Testing Solution2:" << endl;
  test_solution(sol2);
}
