# 2444. Count Subarrays With Fixed Bounds
# Hard
# You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
# A subarray is a contiguous part of an array.
from itertools import groupby


def countSubarrays(nums, minK, maxK):
    left, ans, min_i, max_i = 0, 0, -1, -1

    for right, n in enumerate(nums):
        # Update left & continue
        if minK > n or n > maxK:
            left = right + 1
            continue

        # Update is
        if n == minK:
            min_i = right
        if n == maxK:
            max_i = right

        # Update ans
        if min_i >= left <= max_i:
            ans += min(min_i, max_i) - left + 1

    return ans


# Example 1:
nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
ans = 2
# Explanation: The fixed-bound subarrays are[1, 3, 5] and [1, 3, 5, 2].
print("Pass" if countSubarrays(nums, minK, maxK) == ans else "Fail")
# Example 2:
nums = [1, 1, 1, 1]
minK = 1
maxK = 1
ans = 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
print("Pass" if countSubarrays(nums, minK, maxK) == ans else "Fail")
# Example 3:
nums = [8121, 8121, 955792, 925378, 383928, 673920, 457030, 925378, 925378,
        925378, 92893, 456370, 925378]
minK = 8121
maxK = 925378
ans = 0
print("Pass" if countSubarrays(nums, minK, maxK) == ans else "Fail")
# Example 4:
nums = [89992, 89992, 89992, 900911, 142432, 900911, 900911, 900911, 823426,
        900911, 900911, 308091, 312853, 900911, 900911, 764677, 756995, 89992,
        89992, 188452, 541874, 598970, 900911, 89992, 152245, 193942, 900911,
        89992, 900911, 486074, 508973, 900911, 235617, 44768, 640310, 926517,
        900911, 900911, 489462, 241420, 89992, 339246, 89992, 7549, 292723,
        330338, 986407, 900911, 89992, 900911, 924927, 89992, 354279]
minK = 89992
maxK = 900911
ans = 405
print("Pass" if countSubarrays(nums, minK, maxK) == ans else "Fail")


def countSubarrays(nums, minK, maxK):
    def calc(nums):
        ans, min_i, max_i = 0, None, None

        for idx, n in enumerate(nums):
            if n == minK:
                min_i = idx
            if n == maxK:
                max_i = idx

            if min_i is not None and max_i is not None:
                ans += min(min_i, max_i) + 1
        return ans

    ans = 0
    for g, vs in groupby(nums, key=lambda n: minK <= n <= maxK):
        if g:
            ans += calc(list(vs))

    return ans


# Example 1:
nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
ans = 2
# Explanation: The fixed-bound subarrays are[1, 3, 5] and [1, 3, 5, 2].
print("Pass" if countSubarrays(nums, minK, maxK) == ans else "Fail")
# Example 2:
nums = [1, 1, 1, 1]
minK = 1
maxK = 1
ans = 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
print("Pass" if countSubarrays(nums, minK, maxK) == ans else "Fail")
