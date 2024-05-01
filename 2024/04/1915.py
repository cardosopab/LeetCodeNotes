# 1915. Number of Wonderful Substrings
# Medium
# A wonderful string is a string where at most one letter appears an odd number of times.

# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

# A substring is a contiguous sequence of characters in a string.

class Solution:
    def wounderfulSubstrings(self, word: str) -> int:
        N = len(word)
        orda = ord('a')
        counts = [0] * 2 ** 10
        res = 0
        mask = 0

        counts[0] = 1

        for i in range(N):
            mask ^= (1 << (ord(word[i]) - orda))
            res += counts[mask]
            for j in range(10):
                new_mask = mask ^ (1 << j)
                res += counts[new_mask]
            counts[mask] += 1
        return res


class Solution1:
    def wounderfulSubstrings(self, word: str) -> int:
        counts = [0] * 1024
        res, mask = 0, 0

        counts[0] = 1

        for i in range(len(word)):
            mask ^= (1 << (ord(word[i]) - ord('a')))
            res += counts[mask]
            for j in range(10):
                res += counts[mask ^ (1 << j)]
            counts[mask] += 1
        return res


def test_solutions(solutions):
    for i, sol in enumerate(solutions, start=1):
        # Example 1:
        word = "aba"
        ans = 4
        res = sol().wounderfulSubstrings(word)
        print(res)
        print("Pass" if res == ans else "Fail")
        # Explanation: The four wonderful substrings are underlined below:
        # - "aba" -> "a"
        # - "aba" -> "b"
        # - "aba" -> "a"
        # - "aba" -> "aba"

        # Example 2:
        word = "aabb"
        ans = 9
        res = sol().wounderfulSubstrings(word)
        print(res)
        print("Pass" if res == ans else "Fail")
        # Explanation: The nine wonderful substrings are underlined below:
        # - "aabb" -> "a"
        # - "aabb" -> "aa"
        # - "aabb" -> "aab"
        # - "aabb" -> "aabb"
        # - "aabb" -> "a"
        # - "aabb" -> "abb"
        # - "aabb" -> "b"
        # - "aabb" -> "bb"
        # - "aabb" -> "b"

        # Example 3:
        word = "he"
        ans = 2
        res = sol().wounderfulSubstrings(word)
        print(res)
        print("Pass" if res == ans else "Fail")
        # Explanation: The two wonderful substrings are underlined below:
        # - "he" -> "h"
        # - "he" -> "e"

        # Constraints:
        # 1 <= word.length <= 105
        # word consists of lowercase English letters from 'a' to 'j'.


test_solutions([Solution, Solution1])
