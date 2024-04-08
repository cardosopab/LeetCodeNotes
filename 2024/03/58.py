# 58. Length of Last Word
# Easy
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal
# substring
#  consisting of non-space characters only.
def lengthOfLastWord(s):
    end = len(s) - 1

    while s[end] == " ":
        end -= 1

    start = end
    while start > 0 and s[start - 1] != " ":
        start -= 1

    return end - start + 1


# Example 1:
s = "Hello World"
ans = 5
print("Pass" if lengthOfLastWord(s) == ans else "Fail")
# Explanation: The last word is "World" with length 5.
# Example 2:
s = "   fly me   to   the moon  "
ans = 4
print("Pass" if lengthOfLastWord(s) == ans else "Fail")
# Explanation: The last word is "moon" with length 4.
# Example 3:
s = "luffy is still joyboy"
ans = 6
print("Pass" if lengthOfLastWord(s) == ans else "Fail")
# Explanation: The last word is "joyboy" with length 6.
# Example 4:
s = "a"
ans = 1
print("Pass" if lengthOfLastWord(s) == ans else "Fail")


def lengthOfLastWord(s):
    return len(s.split()[-1])


# Example 1:
s = "Hello World"
ans = 5
print("Pass" if lengthOfLastWord(s) == ans else "Fail")
# Example 2:
s = "   fly me   to   the moon  "
ans = 4
print("Pass" if lengthOfLastWord(s) == ans else "Fail")
# Example 3:
s = "luffy is still joyboy"
ans = 6
print("Pass" if lengthOfLastWord(s) == ans else "Fail")
# Example 4:
s = "a"
ans = 1
print("Pass" if lengthOfLastWord(s) == ans else "Fail")
