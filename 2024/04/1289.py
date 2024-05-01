# from typing import List
# 1289. Minimum Falling Path Sum II
# Hard
# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def get_min_two(row):
            two_smallest = []  # (val, idx)
            for val, idx, in row:
                if len(two_smallest) < 2:
                    two_smallest.append((val, idx))
                elif two_smallest[1][0] > val:
                    two_smallest.pop()
                    two_smallest.append((val, idx))
                two_smallest.sort()
            return two_smallest

        N = len(grid)
        first_row = [(val, idx) for idx, val in enumerate(grid[0])]
        dp = get_min_two(first_row)
        for r in range(1, N):
            next_dp = []  # (val, idx)
            for c in range(N):
                curr_val = grid[r][c]
                min_val = float("inf")
                for prev_val, prev_c in dp:
                    if c != prev_c:
                        min_val = min(min_val, curr_val + prev_val)
                next_dp.append((min_val, c))
                next_dp = get_min_two(next_dp)
            dp = next_dp
        return min([val for val, idx in dp])


# Example 1:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = 13
res = Solution().minFallingPathSum(grid)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.

# Example 2:
grid = [[7]]
ans = 7
res = Solution().minFallingPathSum(grid)
print(res)
print("Pass" if res == ans else "Fail")

# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 200
# -99 <= grid[i][j] <= 99


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        INF = float("inf")
        dp = [[INF] * N for _ in range(N)]

        for j in range(N):
            dp[0][j] = grid[0][j]

        for i in range(1, N):
            for j in range(N):
                for k in range(N):
                    if j != k:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + grid[i][j])
        return min(dp[N-1])


# Example 1:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = 13
res = Solution().minFallingPathSum(grid)
print(res)
print("Pass" if res == ans else "Fail")

# Example 2:
grid = [[7]]
ans = 7
res = Solution().minFallingPathSum(grid)
print(res)
print("Pass" if res == ans else "Fail")


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N, INF = len(grid), float("inf")
        prev_min_1, prev_min_idx_1 = INF, None
        prev_min_2, prev_min_idx_2 = INF, None

        for j in range(N):
            if grid[0][j] < prev_min_1:
                prev_min_2 = prev_min_1
                prev_min_idx_2 = prev_min_idx_1

                prev_min_1 = grid[0][j]
                prev_min_idx_1 = j
            elif grid[0][j] < prev_min_2:
                prev_min_2 = grid[0][j]
                prev_min_idx_2 = j
        for i in range(1, N):
            curr_min_1, curr_min_idx_1 = INF, None
            curr_min_2, curr_min_idx_2 = INF, None
            for j in range(N):
                if j == prev_min_idx_1:
                    curr_val = grid[i][j] + prev_min_2
                else:
                    curr_val = grid[i][j] + prev_min_1
                if curr_val < curr_min_1:
                    curr_min_2 = curr_min_1
                    curr_min_idx_2 = curr_min_idx_1

                    curr_min_1 = curr_val
                    curr_min_idx_1 = j
                elif curr_val < curr_min_2:
                    curr_min_2 = curr_val
                    curr_min_idx_2 = j
            prev_min_1, prev_min_idx_1 = curr_min_1, curr_min_idx_1
            prev_min_2, prev_min_idx_2 = curr_min_2, curr_min_idx_2

        return prev_min_1


# Example 1:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = 13
res = Solution().minFallingPathSum(grid)
print(res)
print("Pass" if res == ans else "Fail")

# Example 2:
grid = [[7]]
ans = 7
res = Solution().minFallingPathSum(grid)
print(res)
print("Pass" if res == ans else "Fail")
