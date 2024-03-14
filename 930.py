# 930. Binary Subarrays With Sum
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
from collections import Counter


def slidingWindow(nums, goal):
    # Count num of subarrs where cursum <= x
    def helper(x):
        if x < 0:
            return 0
        res = 0
        left = cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur > x:
                cur -= nums[left]
                left += 1
            res += (r - left + 1)
        return res
    return helper(goal) - helper(goal - 1)


# Example 1:
nums = [1, 0, 1, 0, 1]
goal = 2
ans = 4
print("Pass" if slidingWindow(nums, goal) == ans else "Fail")
# Example 2:
nums = [0, 0, 0, 0, 0]
goal = 0
ans = 15
print("Pass" if slidingWindow(nums, goal) == ans else "Fail")


def prefixSum(nums, goal):
    f = Counter()
    f[0] = 1
    prefix = ans = 0
    for x in nums:
        prefix += x
        ans += f[prefix - goal]
        f[prefix] += 1
    return ans


# Example 1:
nums = [1, 0, 1, 0, 1]
goal = 2
ans = 4
print("Pass" if prefixSum(nums, goal) == ans else "Fail")
# Example 2:
nums = [0, 0, 0, 0, 0]
goal = 0
ans = 15
print("Pass" if prefixSum(nums, goal) == ans else "Fail")
