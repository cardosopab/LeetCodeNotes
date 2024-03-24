# 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.


def findDuplicates(nums):
    slow, fast = nums[0], nums[0]
    fast = nums[fast]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    start = 0
    while start != slow:
        start = nums[start]
        slow = nums[slow]

    return start


# Example 1:
nums = [1, 3, 4, 2, 2]
ans = 2
print("Pass" if findDuplicates(nums) == ans else "Fail")
# Example 2:
nums = [3, 1, 3, 4, 2]
ans = 3
print("Pass" if findDuplicates(nums) == ans else "Fail")
# Example 3:
nums = [3, 3, 3, 3, 3]
ans = 3
print("Pass" if findDuplicates(nums) == ans else "Fail")
