# 200. Number of Islands
# Medium
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


def numIslands(grid):
    R, C = len(grid), len(grid[0])
    visited = [[False] * C for _ in range(R)]
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    def dfs(r, c):
        visited[r][c] = True
        for dr, dc in directions:
            xr, xc = r + dr, c + dc
            is_greater = xr >= 0 <= xc
            is_less = xr < R and xc < C
            if is_greater and is_less and not visited[xr][xc] and grid[xr][xc] == "1":
                dfs(xr, xc)

    islands = 0
    for r in range(R):
        for c in range(C):
            if not visited[r][c] and grid[r][c] == "1":
                islands += 1
                dfs(r, c)

    print(islands)
    return islands


# Example 1:
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
ans = 1
print("Pass" if numIslands(grid) == ans else "Fail")
# Example 2:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
ans = 3
print("Pass" if numIslands(grid) == ans else "Fail")


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
