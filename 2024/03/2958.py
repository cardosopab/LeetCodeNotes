# 2958. Length of Longest Subarray With at Most K Frequency
# Medium
# You are given an integer array nums and an integer k.
# The frequency of an element x is the number of times it occurs in an array.
# An array is called good if the frequency of each element in this array is less than or equal to k.
# Return the length of the longest good subarray of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.

from collections import defaultdict


def maxSubarrayLength(nums, k):
    # Sliding Window
    # Using a dictionary
    # Count value occurrence
    # Slide left pointer if value count is over k
    count = defaultdict(int)
    length = 1
    left = 0

    for right, right_number in enumerate(nums):
        left_number = nums[left]
        count[right_number] += 1

        while left < right and count[right_number] > k:
            count[left_number] -= 1
            left += 1
        interval_length = right - left + 1
        length = max(length, interval_length)

    return length


# Example 1:
nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
ans = 6
print("Pass" if maxSubarrayLength(nums, k) == ans else "Fail")
# Example 2:
nums = [1, 2, 1, 2, 1, 2, 1, 2]
k = 1
ans = 2
print("Pass" if maxSubarrayLength(nums, k) == ans else "Fail")
# Example 3:
nums = [5, 5, 5, 5, 5, 5, 5]
k = 4
ans = 4
print("Pass" if maxSubarrayLength(nums, k) == ans else "Fail")
# Example 4:
nums = [1, 4, 4, 3]
k = 1
ans = 2
print("Pass" if maxSubarrayLength(nums, k) == ans else "Fail")
# Example 5:
nums = [1]
k = 1
ans = 1
print("Pass" if maxSubarrayLength(nums, k) == ans else "Fail")
# Example 6:
nums = [1, 11]
k = 2
ans = 2
print("Pass" if maxSubarrayLength(nums, k) == ans else "Fail")
# Example 7:
nums = [2, 2, 3]
k = 1
ans = 2
print("Pass" if maxSubarrayLength(nums, k) == ans else "Fail")
