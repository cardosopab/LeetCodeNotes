# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.

# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s, t):
        slow = fast = 0

        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1

        return True if slow == len(s) else False


# Example 1:
s = "abc"
t = "ahbgdc"
output = True
print("Pass" if Solution().isSubsequence(s, t) == output else "Fail")

# Example 2:
s = "axc"
t = "ahbgdc"
output = False
print("Pass" if Solution().isSubsequence(s, t) == output else "Fail")
