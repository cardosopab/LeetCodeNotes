# 2962. Count Subarrays Where Max Element Appears at Least K Times
# Medium
# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.


def countSubarrays(nums, k):
    left, res, count, max_n = 0, 0, 0, max(nums)

    for right in range(len(nums)):
        if nums[right] == max_n:
            count += 1

        while count >= k:
            if nums[left] == max_n:
                count -= 1
            left += 1

        res += left

    print(res)
    return res


# Example 1:
nums = [1, 3, 2, 3, 3]
k = 2
ans = 6
print("Pass" if countSubarrays(nums, k) == ans else "Fail")
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
# Example 2:
nums = [1, 4, 2, 1]
k = 3
ans = 0
print("Pass" if countSubarrays(nums, k) == ans else "Fail")
# Explanation: No subarray contains the element 4 at least 3 times.
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105


def countSubarrays(nums, k):
    left, right, best, count, maxEl = 0, 0, 0, 0, max(nums)

    for right in range(len(nums)):
        if nums[right] == maxEl:
            count += 1
        while count > k or (left <= right and count == k and nums[left] != maxEl):
            if nums[left] == maxEl:
                count -= 1
            left += 1
        if count == k:
            best += left + 1

    print(best)
    return best


# Example 1:
nums = [1, 3, 2, 3, 3]
k = 2
ans = 6
print("Pass" if countSubarrays(nums, k) == ans else "Fail")
# Example 2:
nums = [1, 4, 2, 1]
k = 3
ans = 0
print("Pass" if countSubarrays(nums, k) == ans else "Fail")
