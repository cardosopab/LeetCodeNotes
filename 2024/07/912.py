# 912. Sort an Array
# Medium
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

from typing import List
from collections import deque
from itertools import islice


class Solution:
    def merge(self, nums):
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        first, second = self.merge(nums[:mid]), self.merge(nums[mid:])
        ans = []

        while first and second:
            if first[0] < second[0]:
                ans.append(first.pop(0))
            else:
                ans.append(second.pop(0))

        ans.extend(first)
        ans.extend(second)

        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge(nums)


class Solution1:
    def merge(self, nums):
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        first, second = deque(self.merge(nums[:mid])), deque(
            self.merge(nums[mid:]))
        ans = []

        while first and second:
            if first[0] < second[0]:
                ans.append(first.popleft())
            else:
                ans.append(second.popleft())

        ans.extend(first)
        ans.extend(second)

        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge(nums)


# Example 1:
nums = [5, 2, 3, 1]
ans = [1, 2, 3, 5]
res = Solution().sortArray(nums)
res1 = Solution1().sortArray(nums)
print("Pass" if ans == res else "Fail")
print("Pass" if ans == res1 else "Fail")
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:
nums = [5, 1, 1, 2, 0, 0]
ans = [0, 0, 1, 1, 2, 5]
res = Solution().sortArray(nums)
res1 = Solution1().sortArray(nums)
print("Pass" if ans == res else "Fail")
print("Pass" if ans == res1 else "Fail")
# Explanation: Note that the values of nums are not necessairly unique.


# Constraints:
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
