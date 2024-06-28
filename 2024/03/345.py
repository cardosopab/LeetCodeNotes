# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Input: string
# Output: string with the vowels reversed
# Solution: use two pointers, move from out to in, if vowels switch characters
def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    c = list(s)
    N = len(c)
    left, right = 0, N - 1

    while left < right:
        while left < N and c[left].lower() not in vowels:
            left += 1

        while right >= 0 and c[right].lower() not in vowels:
            right -= 1

        if left < right:
            c[left], c[right] = c[right], c[left]
            left += 1
            right -= 1

    print("".join(c))
    return "".join(c)


# Example 1:
s = "hello"
ans = "holle"
print("Pass" if reverseVowels(s) == ans else "Fail")
# Example 2:
s = "leetcode"
ans = "leotcede"
print("Pass" if reverseVowels(s) == ans else "Fail")
# Example 3:
s = "aA"
ans = "Aa"
print("Pass" if reverseVowels(s) == ans else "Fail")
# Example 4:
s = "Euston saw I was not Sue."
ans = "euston saw I was not SuE."
print("Pass" if reverseVowels(s) == ans else "Fail")
