# 1408. String Matching in an Array
# Easy
# Topics
# Companies
# Hint
# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
#
# A substring is a contiguous sequence of characters within a string
#

class Solution:
    def stringMatching(self, words):
        res = []
        N = len(words)
        for i in range(N):
            for j in range(N):
                if i != j:
                    if (words[i] in words[j]):
                        res.append(words[i])
        return res


#
# Example 1:
words = ["mass", "as", "hero", "superhero"]
ans = ["as", "hero"]
print("Pass" if Solution().stringMatching(words) == ans else "Fail")
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
words = ["leetcode", "et", "code"]
ans = ["et", "code"]
print("Pass" if Solution().stringMatching(words) == ans else "Fail")
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:
words = ["blue", "green", "bu"]
ans = []
print("Pass" if Solution().stringMatching(words) == ans else "Fail")
# Explanation: No string of words is substring of another string.
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.
