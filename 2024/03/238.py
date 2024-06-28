# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    N = len(nums)

    def get_prefix_product(arr):
        prefix = [1]
        for x in arr:
            prefix.append(prefix[-1]*x)
        return prefix

    prefix = get_prefix_product(nums)
    suffix = get_prefix_product(nums[::-1])
    suffix.reverse()

    ans = []

    for i in range(N):
        ans.append(prefix[i] * suffix[i+1])
    return ans


# Example 1:
nums = [1, 2, 3, 4]
ans = [24, 12, 8, 6]
print("Pass" if productExceptSelf(nums) == ans else "Fail")
# Example 2:
nums = [-1, 1, 0, -3, 3]
ans = [0, 0, 9, 0, 0]
print("Pass" if productExceptSelf(nums) == ans else "Fail")
