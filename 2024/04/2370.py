# 2370. Longest Ideal Subsequence
# Medium
# You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:
#
# t is a subsequence of the string s.
# The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
# Return the length of the longest ideal string.
#
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
#
# Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        orda = ord("a")

        for c in s:
            ordc = ord(c) - orda
            length = 1

            for i in range(26):
                if abs(ordc - i) <= k:
                    length = max(length, 1 + dp[i])

            dp[ordc] = max(length, 1 + dp[ordc])
        return max(dp)


class Solution1:
    def longestIdealString(self, s: str, k: int) -> int:
        ranges = {}
        orda = ord("a")

        for c in s:
            ordc = ord(c) - orda
            length = 1

            if ranges:
                for i in range(26):
                    if i in ranges and abs(ordc - i) <= k:
                        length = max(length, 1 + ranges[i])

            ranges[ordc] = length

        return max(ranges.values())


class Solution2:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        orda = ord("a")

        for c in s:
            ordc = ord(c) - orda
            length = 1

            start = max(0, ordc - k - 1)
            end = min(26, ordc + k + 1)

            for i in range(start, end):
                if abs(ordc - i) <= k:
                    length = max(length, 1 + dp[i])
            dp[ordc] = max(length, 1 + dp[ordc])
        return max(dp)


def test_solutions(solutions: list):
    for i, sol in enumerate(solutions, start=1):
        print(f"Solution: {i}")
        # Example 1:
        s = "acfgbd"
        k = 2
        ans = 4
        res = sol().longestIdealString(s, k)
        print(res)
        print("Pass" if res == ans else "Fail")
        # Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
        # Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

        # Example 2:
        s = "abcd"
        k = 3
        ans = 4
        res = sol().longestIdealString(s, k)
        print(res)
        print("Pass" if res == ans else "Fail")
        # Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

        # Example 3:
        s = "jxhwaysa"
        k = 14
        ans = 5
        res = sol().longestIdealString(s, k)
        print(res)
        print("Pass" if res == ans else "Fail")

        # Example 4:
        s = "azaza"
        k = 25
        ans = 5
        res = sol().longestIdealString(s, k)
        print(res)
        print("Pass" if res == ans else "Fail")

        # Example 5:
        s = "lopjigzbaq"
        k = 5
        ans = 7
        res = sol().longestIdealString(s, k)
        print(res)
        print("Pass" if res == ans else "Fail")

        # Example 6:
        s = "fqyokqgzvjpermqmwcjqtzbxnurjmawsswlwzmnjbbhdtfjxnktwtonpeorewc"
        k = 3
        ans = 19
        res = sol().longestIdealString(s, k)
        print(res)
        print("Pass" if res == ans else "Fail")

        # Constraints:
        # 1 <= s.length <= 105
        # 0 <= k <= 25
        # s consists of lowercase English letters.


test_solutions([Solution, Solution1, Solution2])
