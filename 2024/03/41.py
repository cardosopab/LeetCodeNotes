# 41. First Missing Positive
# Hard
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


def firstMissingPositive(nums):
    N = len(nums)

    # Permutation Cycle
    # Cycle Sorting
    for i in range(N):
        while True:
            x = nums[i]
            if x <= 0 or x > N or nums[x - 1] == x:
                break
            nums[i], nums[x-1] = nums[x-1], nums[i]

    for i in range(N):
        if nums[i] != i + 1:
            return i + 1
    return N + 1


# Example 1:
nums = [1, 2, 0]
ans = 3
print("Pass" if firstMissingPositive(nums) == ans else "Fail")
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:
nums = [3, 4, -1, 1]
ans = 2
print("Pass" if firstMissingPositive(nums) == ans else "Fail")
# Explanation: 1 is in the array but 2 is missing.
# Example 3:
nums = [7, 8, 9, 11, 12]
ans = 1
print("Pass" if firstMissingPositive(nums) == ans else "Fail")
# Explanation: The smallest positive integer 1 is missing.
