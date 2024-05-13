# 861. Score After Flipping Matrix
# Medium
# You are given an m x n binary matrix grid.
#
# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
#
# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
#
# Return the highest possible score after making any number of moves (including zero moves).


class Solution:
    def matrixScore(self, grid):
        R, C, ans = len(grid), len(grid[0]), 0

        for r in range(R):
            if grid[r][0] == 0:
                for c in range(C):
                    grid[r][c] = 1 - grid[r][c]

        for c in range(C):
            ones, zeros = 0, 0
            for r in range(R):
                if grid[r][c] == 0:
                    zeros += 1
                else:
                    ones += 1
            ans += (2 ** (C - 1 - c)) * max(ones, zeros)

        return ans


# Example 1:
grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
ans = 39
res = Solution().matrixScore(grid)
print("Pass" if res == ans else f"Fail {res}")
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

# Example 2:
grid = [[0]]
ans = 1
res = Solution().matrixScore(grid)
print("Pass" if res == ans else f"Fail {res}")

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid[i][j] is either 0 or 1.
