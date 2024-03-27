# 713. Subarray Product Less Than K
# Medium
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
def numSubarrayProductLessThanK(nums, k):
    res, left, product, N = 0, 0, 1, len(nums)

    for right in range(N):
        product *= nums[right]
        while left <= right and product >= k:
            product //= nums[left]
            left += 1
        res += (right - left + 1)
    return res


# Example 1:
nums = [10, 5, 2, 6]
k = 100
ans = 8
print("Pass" if numSubarrayProductLessThanK(nums, k) == ans else "Fail")
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:
nums = [1, 2, 3]
k = 0
ans = 0
print("Pass" if numSubarrayProductLessThanK(nums, k) == ans else "Fail")
