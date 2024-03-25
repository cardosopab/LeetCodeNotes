# 442. Find All Duplicates in an Array
# Medium
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

def findDuplicates(nums):
    res = []

    for n in nums:
        n = abs(n)
        curr = nums[n-1]
        if curr < 0:
            res.append(n)
        nums[n-1] = -curr
    return res


# Example 1:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
ans = [2, 3]
print("Pass"if findDuplicates(nums) == ans else "Fail")
# Example 2:
nums = [1, 1, 2]
ans = [1]
print("Pass"if findDuplicates(nums) == ans else "Fail")
# Example 3:
nums = [1]
ans = []
print("Pass"if findDuplicates(nums) == ans else "Fail")


def findDuplicates(nums):
    B = (10 ** 5) + 1
    res = []
    for n in nums:
        idx = (n % B) - 1
        nums[idx] += B

    for i, n in enumerate(nums):
        if n > 2 * B:
            res.append(i + 1)

    return res


# Example 1:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
ans = [2, 3]
print("Pass"if findDuplicates(nums) == ans else "Fail")
# Example 2:
nums = [1, 1, 2]
ans = [1]
print("Pass"if findDuplicates(nums) == ans else "Fail")
# Example 3:
nums = [1]
ans = []
print("Pass"if findDuplicates(nums) == ans else "Fail")
