# 791. Custom Sort String
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Input: order string, and s string
# Output: custom ordered string
# Solution: iterate through order string pulling the matches out, and into the ans array, return ans plus the remaining s string

def customSortString(order, s):
    ans = []
    for c in order:
        while c in s:
            ans.append(c)
            s = s.replace(c, "", 1)

    return "".join(ans) + s


# Example 1:
order = "cba"
s = "abcd"
ans = "cbad"
print("Pass" if customSortString(order, s) == ans else "Fail")
# Example 2:
order = "bcafg"
s = "abcd"
ans = "bcad"
print("Pass" if customSortString(order, s) == ans else "Fail")
# Example 3:
order = "kqep"
s = "pekeq"
ans = "kqeep"
print("Pass" if customSortString(order, s) == ans else "Fail")
