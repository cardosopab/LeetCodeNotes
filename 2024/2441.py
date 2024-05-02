# 2441. Largest Positive Integer That Exists With Its Negative
# Easy
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.


from typing import List
import time


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] >= 0:
                return -1
            if abs(nums[left]) == nums[right]:
                return nums[right]
            if abs(nums[left]) > nums[right]:
                left += 1
            else:
                right -= 1

        return -1


def test_solutions(solutions: Solution):
    for i, sol in enumerate(solutions):
        print(f"Solution {i}")

        # Example 1:
        nums = [-1, 2, -3, 3]
        ans = 3
        start_time = time.time()
        res = sol().findMaxK(nums)
        stop_time = time.time()
        print(
            f"Pass: {res} Time:{stop_time -start_time:.6f}" if ans == res else f"Fail: {res}")
        # Explanation: 3 is the only valid k we can find in the array.

        # Example 2:
        nums = [-1, 10, 6, 7, -7, 1]
        ans = 7
        start_time = time.time()
        res = sol().findMaxK(nums)
        stop_time = time.time()
        print(
            f"Pass: {res} Time:{stop_time -start_time:.6f}" if ans == res else f"Fail: {res}")
        # Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

        # Example 3:
        nums = [-10, 8, 6, 7, -2, -3]
        ans = -1
        start_time = time.time()
        res = sol().findMaxK(nums)
        stop_time = time.time()
        print(
            f"Pass: {res} Time:{stop_time -start_time:.6f}" if ans == res else f"Fail: {res}")
        # Explanation: There is no a single valid k, we return -1.

        # Example 3:
        nums = [1000, 1000]
        ans = -1
        start_time = time.time()
        res = sol().findMaxK(nums)
        stop_time = time.time()
        print(
            f"Pass: {res} Time:{stop_time -start_time:.6f}" if ans == res else f"Fail: {res}")

        # Constraints:
        # 1 <= nums.length <= 1000
        # -1000 <= nums[i] <= 1000
        # nums[i] != 0
test_solutions([Solution])
