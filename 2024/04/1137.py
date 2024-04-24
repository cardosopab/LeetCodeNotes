# 1137. N-th Tribonacci Number
# Easy
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.


from functools import cache


class Solution:
    def tribonacci(self, n: int) -> int:
        has_cache = [False] * (n + 1)
        cache = [None] * (n + 1)

        def calc(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if has_cache[n]:
                return cache[n]
            cache[n] = calc(n - 1) + calc(n - 2) + calc(n - 3)
            has_cache[n] = True
            return cache[n]

        return calc(n)


# Example 1:
n = 4
ans = 4
res = Solution().tribonacci(n)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
n = 25
ans = 1389537
res = Solution().tribonacci(n)
print(res)
print("Pass" if res == ans else "Fail")

# Example 3:
n = 37
ans = 2082876103
res = Solution().tribonacci(n)
print(res)
print("Pass" if res == ans else "Fail")

# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


class Solution:
    def tribonacci(self, n: int) -> int:

        @cache
        def calc(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            return calc(n - 1) + calc(n - 2) + calc(n - 3)

        return calc(n)


# Example 1:
n = 4
ans = 4
res = Solution().tribonacci(n)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
n = 25
ans = 1389537
res = Solution().tribonacci(n)
print(res)
print("Pass" if res == ans else "Fail")

# Example 3:
n = 37
ans = 2082876103
res = Solution().tribonacci(n)
print(res)
print("Pass" if res == ans else "Fail")

# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
