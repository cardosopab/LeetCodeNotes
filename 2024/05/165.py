# 165. Compare Version Numbers
# Medium
# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.


from collections import deque


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)

        for a, b in zip(v1, v2):
            a, b = int(a), int(b)
            if a == b:
                continue
            if a > b:
                return 1
            else:
                return -1
        return 0


# Example 1:
version1 = "1.01"
version2 = "1.001"
ans = 0
res = Solution().compareVersion(version1, version2)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

# Example 2:
version1 = "1.0"
version2 = "1.0.0"
ans = 0
res = Solution().compareVersion(version1, version2)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: version1 does not specify revision 2, which means it is treated as "0".

# Example 3:
version1 = "0.1"
version2 = "1.1"
ans = -1
res = Solution().compareVersion(version1, version2)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

# Example 3:
version1 = "1.1"
version2 = "1.10"
ans = -1
res = Solution().compareVersion(version1, version2)
print(res)
print("Pass" if res == ans else "Fail")

# Example 3:
version1 = "1.0.1"
version2 = "1"
ans = 1
res = Solution().compareVersion(version1, version2)
print(res)
print("Pass" if res == ans else "Fail")

# Constraints:
# 1 <= version1.length
# version2.length <= 500
# version1 and version2 only contain digits and '.'.
# version1 and version2 are valid version numbers.
# All the given revisions in version1 and version2 can be stored in a 32-bit integer.
