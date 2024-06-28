# 2540. Minimum Common Value
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

# Input: two arrays of numbers
# Output: min common value between two arrays
# Solution: use two pointers to check which is the min match
class Solution:
    def getCommon(self, nums1, nums2):
        left = right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                return nums1[left]
            if nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return -1


# Example 1:
nums1 = [1, 2, 3]
nums2 = [2, 4]
ans = 2
print("Pass" if Solution().getCommon(nums1, nums2) == ans else "Fail")
# Example 2:
nums1 = [1, 2, 3, 6]
nums2 = [2, 3, 4, 5]
ans = 2
print("Pass" if Solution().getCommon(nums1, nums2) == ans else "Fail")
# Example 3:
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
ans = -1
print("Pass" if Solution().getCommon(nums1, nums2) == ans else "Fail")
