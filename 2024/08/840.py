# 840. Magic Squares In Grid
# Medium
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C, ans = len(grid), len(grid[0]), 0

        def is_magic(r, c):
            nums = {grid[r + i][c + j] for i in range(3) for j in range(3)}
            if nums != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False

            val = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
            for i in range(1, 3):
                curr = grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2]
                if val != curr:
                    return False

            for j in range(3):
                curr = grid[r][c + j] + grid[r + 1][c + j] + grid[r + 2][c + j]
                if val != curr:
                    return False

            if (
                grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != val
                or grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != val
            ):
                return False

            return True

        for r in range(R - 2):
            for c in range(C - 2):
                if is_magic(r, c):
                    ans += 1

        return ans


# Example 1:
grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
ans = 1
res = Solution().numMagicSquaresInside(grid)
print("Pass" if ans == res else "Fail")
# Explanation:
# The following subgrid is a 3 x 3 magic square:
# while this one is not:
# In total, there is only one magic square inside the given grid.

# Example 2:
grid = [[8]]
ans = 0
res = Solution().numMagicSquaresInside(grid)
print("Pass" if ans == res else "Fail")


# Example 3:
grid = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
ans = 0
res = Solution().numMagicSquaresInside(grid)
print("Pass" if ans == res else "Fail")

# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
