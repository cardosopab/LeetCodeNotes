# 205. Isomorphic Strings
# Easy
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    lookup = {}
    rlookup = {}

    for sc, tc, in zip(s, t):
        if sc not in lookup:
            lookup[sc] = tc
        if tc not in rlookup:
            rlookup[tc] = sc

        if lookup[sc] != tc or rlookup[tc] != sc:
            return False
    return True


# Example 1:
s = "egg"
t = "add"
ans = True
print("Pass" if isIsomorphic(s, t) == ans else "Fail")
# Example 2:
s = "foo"
t = "bar"
ans = False
print("Pass" if isIsomorphic(s, t) == ans else "Fail")
# Example 3:
s = "paper"
t = "title"
ans = True
print("Pass" if isIsomorphic(s, t) == ans else "Fail")
# Example 4:
s = "bbbaaaba"
t = "aaabbbba"
ans = False
print("Pass" if isIsomorphic(s, t) == ans else "Fail")
# Example 5:
s = "badc"
t = "baba"
ans = False
print("Pass" if isIsomorphic(s, t) == ans else "Fail")
