# 992. Subarrays with K Different Integers
# Hard
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1, 2, 3, 1, 2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
from collections import defaultdict
from collections import Counter


def subarrayWithKDistinct(nums, k):
    far, near, res, count = 0, 0, 0, defaultdict(int)

    for right in range(len(nums)):
        count[nums[right]] += 1

        while len(count) > k:
            #             count[nums[near]] -= 1
            #             if count[nums[near]] == 0:
            #                 count.pop(nums[near])
            count.pop(nums[near])
            near += 1
            far = near

        while count[nums[near]] > 1:
            count[nums[near]] -= 1
            near += 1

        if len(count) == k:
            res += near - far + 1
    return res


# Example 1:
nums = [1, 2, 1, 2, 3]
k = 2
ans = 7
# Explanation: Subarrays formed with exactly 2 different integers: [1, 2], [2, 1], [1, 2], [2, 3], [1, 2, 1], [2, 1, 2], [1, 2, 1, 2]
print("Pass" if subarrayWithKDistinct(nums, k) == ans else "Fail")
# Example 2:
nums = [1, 2, 1, 3, 4]
k = 3
ans = 3
# Explanation: Subarrays formed with exactly 3 different integers: [1, 2, 1, 3], [2, 1, 3], [1, 3, 4].
print("Pass" if subarrayWithKDistinct(nums, k) == ans else "Fail")


def subarrayWithKDistinct(nums, k):
    def subarrayWithKOrLess(nums, k):
        left, total, N, count = 0, 0, len(nums), Counter()

        for right in range(N):
            right_n = nums[right]
            count[right_n] += 1

            while len(count) > k:
                left_n = nums[left]
                count[left_n] -= 1
                if count[left_n] == 0:
                    del count[left_n]
                left += 1

            total += right - left + 1

        return total
    ans = subarrayWithKOrLess(nums, k) - subarrayWithKOrLess(nums, k - 1)
    print(ans)
    return ans


# Example 1:
nums = [1, 2, 1, 2, 3]
k = 2
ans = 7
print("Pass" if subarrayWithKDistinct(nums, k) == ans else "Fail")
# Example 2:
nums = [1, 2, 1, 3, 4]
k = 3
ans = 3
print("Pass" if subarrayWithKDistinct(nums, k) == ans else "Fail")
