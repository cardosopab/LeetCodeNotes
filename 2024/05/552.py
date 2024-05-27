# 552. Student Attendance Record II
# Hard
# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
 
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
 
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 
import sys
sys.setrecursionlimit(20000)

from collections import defaultdict


class Solution:
    def checkRecord(self, N):
        MOD = 10 ** 9 + 7

        has_cache = [[[False] * 3 for _ in range(2)] for _ in range(N)]
        cache = [[[None] * 3 for _ in range(2)] for _ in range(N)]

        def count(days, absences, late):
            if days == N:
                return 1

            if has_cache[days][absences][late]:
                return cache[days][absences][late]

            total = 0

            # "P" day
            total += count(days + 1, absences, 0)

            # "A" day
            if absences < 1:
                total += count(days + 1, absences + 1, 0)

            # "L" day
            if late < 2:
                total += count(days + 1, absences, late + 1)

            has_cache[days][absences][late] = True
            cache[days][absences][late] = total % MOD
            return cache[days][absences][late]
        
        return count(0, 0, 0)

# Example 1:
n = 2
ans = 8
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

# Example 2:
n = 1
ans = 3
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")

# Example 3:
n = 10101
ans = 183236316
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")

# Constraints:
# 1 <= n <= 105


class Solution:
    def checkRecord(self, N):
        MOD = 10 ** 9 + 7

        cache = {}

        def count(N):
            if N == 1:
                return {
                    (0, 0): 1, (0, 1): 1, (0, 2): 0,
                    (1, 0): 1, (1, 1): 0, (1, 2): 0,
                }

            if N in cache:
                return cache[N]

            tmp = count(N - 1)
            res = defaultdict(int)

            # "P" day
            res[(0, 0)] = ((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)]) % MOD
            res[(1, 0)] = ((tmp[(1, 0)] + tmp[(1, 1)]) % MOD + tmp[(1, 2)]) % MOD

            # "L" day
            res[(0,1)] = tmp[(0,0)]
            res[(1,1)] = tmp[(1,0)]
            res[(0,2)] = tmp[(0,1)]
            res[(1,2)] = tmp[(1,1)]

            # "A" day
            res [(1, 0)] = (res[(1, 0)] + (((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)])) % MOD) % MOD
            cache[N] = res
            return cache[N]
        
        return sum(count(N).values()) % MOD

# Example 1:
n = 2
ans = 8
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")

# Example 2:
n = 1
ans = 3
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")

# Example 3:
n = 10101
ans = 183236316
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")


class Solution:
    def checkRecord(self, N):
        MOD = 10 ** 9 + 7

        if N == 1:
            return 3

        res = {
            (0, 0): 1, (0, 1): 1, (0, 2): 0,
            (1, 0): 1, (1, 1): 0, (1, 2): 0,
        }

        for i in range(N - 1):
            temp = defaultdict(int)

            # "P" day
            temp[(0, 0)] = ((res[(0, 0)] + res[(0, 1)]) % MOD + res[(0, 2)]) % MOD
            temp[(1, 0)] = ((res[(1, 0)] + res[(1, 1)]) % MOD + res[(1, 2)]) % MOD

            # "L" day
            temp[(0,1)] = res[(0,0)]
            temp[(1,1)] = res[(1,0)]
            temp[(0,2)] = res[(0,1)]
            temp[(1,2)] = res[(1,1)]

            # "A" day
            temp [(1, 0)] = (temp[(1, 0)] + (((res[(0, 0)] + res[(0, 1)]) % MOD + res[(0, 2)])) % MOD) % MOD
            res = temp
        
        return sum(res.values()) % MOD

# Example 1:
n = 2
ans = 8
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")

# Example 2:
n = 1
ans = 3
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")

# Example 3:
n = 10101
ans = 183236316
res = Solution().checkRecord(n)
print("Pass" if ans == res else f"Fail: {res}")
