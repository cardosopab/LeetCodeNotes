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
        res = set()
        for w in words:
            for x in words:
                if w is not x and w in x:
                    res.add(w)
        return list(res)


def equal_lists(ans, sol):
    if len(ans) != len(sol):
        return False
    for w in ans:
        if w not in sol:
            return False
    return True


#
# Example 1:
words = ["mass", "as", "hero", "superhero"]
ans = ["as", "hero"]
valid = equal_lists(ans, Solution().stringMatching(words))
print("Pass" if valid else "Fail")
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
words = ["leetcode", "et", "et", "code"]
ans = ["et", "code"]
valid = equal_lists(ans, Solution().stringMatching(words))
print("Pass" if valid else "Fail")
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:
words = ["blue", "green", "bu"]
ans = []
valid = equal_lists(ans, Solution().stringMatching(words))
print("Pass" if valid else "Fail")
# Explanation: No string of words is substring of another string.
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.
