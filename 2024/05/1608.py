# 1608. Special Array With X Elements Greater Than or Equal X
# Easy
# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
# 
# Notice that x does not have to be an element in nums.
# 
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 
from collections import Counter
class Solution:
    def specialArray(self, nums):
        N = len(nums)
        max_n = max(nums)
        buckets = [0] * (max_n + 1)

        for n in nums:
            buckets[n] += 1

        best = 0
        for i in range(max_n, -1, - 1):
            print(i)
            best += buckets[i]
            if i == best:
                return i

        return -1

# Example 1:
nums = [3,5]
ans = 2
res = Solution().specialArray(nums)
print("Pass" if ans == res else f"Fail: {res}")
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# Example 2:
nums = [0,0]
ans = -1
res = Solution().specialArray(nums)
print("Pass" if ans == res else f"Fail: {res}")
# Explanation: No numbers fit the criteria for x.
# If x = 0, there should be 0 numbers >= x, but there are 2.
# If x = 1, there should be 1 number >= x, but there are 0.
# If x = 2, there should be 2 numbers >= x, but there are 0.
# x cannot be greater since there are only 2 numbers in nums.

# Example 3:
nums = [0,4,3,0,4]
ans = 3
res = Solution().specialArray(nums)
print("Pass" if ans == res else f"Fail: {res}")
# Explanation: There are 3 values that are greater than or equal to 3.

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
