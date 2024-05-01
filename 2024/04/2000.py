# 2000. Reverse Prefix of Word
# Easy
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.


import time
from collections import deque


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        res = []
        idx = word.index(ch)
        for i in range(idx, -1, -1):
            res.append(word[i])
        for j in range(idx + 1, len(word)):
            res.append(word[j])
        return "".join(res)


class Solution1:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx, N, d = None, len(word), deque()

        for i in range(N):
            d.appendleft(word[i])
            if word[i] == ch:
                idx = i
                break

        if not idx:
            return word

        for j in range(idx + 1, len(word)):
            d.append(word[j])
        return "".join(d)


class Solution2:
    def reversePrefix(self, word: str, ch: str) -> str:
        found, d = False, deque()

        for i, c in enumerate(word):
            if not found:
                d.appendleft(c)
                if c == ch:
                    found = True

            elif found:
                d.append(c)

        if not found:
            return word

        return "".join(d)


class Solution3:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = list(word)

        for i, c in enumerate(ans):
            if c == ch:
                left, right = 0, i
                while left < right:
                    ans[left], ans[right] = ans[right], ans[left]
                    left += 1
                    right -= 1
                break

        return "".join(ans)


class Solution4:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch)
        except ValueError:
            return word
        return word[: index + 1][::-1] + word[index + 1 :]


def test_solutions(solutions: Solution):
    for i, sol in enumerate(solutions):
        print(f"Solution {i}")
        # Example 1:
        word = "abcdefd"
        ch = "d"
        ans = "dcbaefd"
        start_time = time.time()
        res = sol().reversePrefix(word, ch)
        end_time = time.time()
        # print(res)
        print("Pass" if res == ans else "Fail")
        print(f"Time taken: {end_time - start_time:.6f} seconds")

        # Explanation: The first occurrence of "d" is at index 3.
        # Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

        # Example 2:
        word = "xyxzxe"
        ch = "z"
        ans = "zxyxxe"
        start_time = time.time()
        res = sol().reversePrefix(word, ch)
        end_time = time.time()
        # print(res)
        print("Pass" if res == ans else "Fail")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        # Explanation: The first and only occurrence of "z" is at index 3.
        # Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

        # Example 3:
        word = "abcd"
        ch = "z"
        ans = "abcd"
        start_time = time.time()
        res = sol().reversePrefix(word, ch)
        end_time = time.time()
        # print(res)
        print("Pass" if res == ans else "Fail")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        # Explanation: "z" does not exist in word.
        # You should not do any reverse operation, the resulting string is "abcd".

        # Constraints:
        # 1 <= word.length <= 250
        # word consists of lowercase English letters.
        # ch is a lowercase English letter.


test_solutions([Solution, Solution1, Solution2, Solution3, Solution4])
