# 1219. Path with Maximum Gold
# Medium
# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
#
# Return the maximum amount of gold you can collect under the conditions:
#
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.


class Solution:
    def getMaximumGold(self, grid):
        ans, R, C = 0, len(grid), len(grid[0])

        def dfs(r, c):
            is_greater = r >= R or c >= C
            is_less = r < 0 or c < 0
            if is_greater or is_less or grid[r][c] == 0:
                return 0
            curr = grid[r][c]
            grid[r][c] = 0

            res = max(dfs(r+1, c), dfs(r, c+1), dfs(r-1, c), dfs(r, c-1))

            grid[r][c] = curr
            return res + curr

        for r in range(R):
            for c in range(C):
                ans = max(ans, dfs(r, c))

        return ans


# Example 1:
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
ans = 24
res = Solution().getMaximumGold(grid)
print("Pass" if res == ans else f"Fail {res}")
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.

# Example 2:
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
ans = 28
res = Solution().getMaximumGold(grid)
print("Pass" if res == ans else f"Fail {res}")
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.
