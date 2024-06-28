# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Input: two arrays
# Output: array with intersecting numbers
# Solution: create sets for each array, and check inclusions

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    ans = []

    shortSet = set1 if len(set1) <= len(set2) else set2
    longSet = set2 if len(set2) >= len(set1) else set1
    print(shortSet)
    print(longSet)

    for n in shortSet:
        if n in longSet:
            ans.append(n)

    print(ans)
    return ans


# Example 1:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
ans = [2]
print("Pass" if intersection(nums1, nums2) == ans else "Fail")
# Example 2:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
ans = [9, 4]
print("Pass" if intersection(nums1, nums2) == ans else "Fail")
# Example 3:
nums1 = [4, 7, 9, 7, 6, 7]
nums2 = [5, 0, 0, 6, 1, 6, 2, 2, 4]
ans = [4, 6]
print("Pass" if intersection(nums1, nums2) == ans else "Fail")
