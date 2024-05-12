# 4. Median of Two Sorted Arrays
# Hard
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    if len(B) < len(A):
        A, B = B, A

    lenA, lenB = len(A), len(B)
    total, half = lenA + lenB, (lenA + lenB) // 2
    left, right = 0, lenA - 1

    while True:
        i = (left + right) // 2  # A
        j = half - i - 2  # B

        Aleft = A[i] if i >= 0 else float("-inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Aright = A[i + 1] if (i + 1) < lenA else float("inf")
        Bright = B[j + 1] if (j + 1) < lenB else float("inf")

        # Partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # Odd
            if total % 2:
                return min(Aright, Bright)
            # Even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            right = i - 1
        else:
            left = i + 1


# Example 1
nums1 = [1, 3]
nums2 = [2]
ans = 2.00000
res = findMedianSortedArrays(nums1, nums2)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
ans = 2.50000
res = findMedianSortedArrays(nums1, nums2)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i]
# nums2[i] <= 106
