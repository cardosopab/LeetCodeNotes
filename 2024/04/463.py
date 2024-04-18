# 463. Island Perimeter
# Easy
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


def islandPerimeter(grid):
    R, C = len(grid), len(grid[0])
    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]
    ans = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                for dr, dc in directions:
                    xr = r + dr
                    xc = c + dc
                    is_greater = xr >= 0 <= xc
                    is_less = xr < R and xc < C

                    if is_greater and is_less:
                        if grid[xr][xc] == 0:
                            ans += 1
                    elif is_greater:
                        ans += 1
                    elif is_less:
                        ans += 1
    return ans


# Example 1:
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
ans = 16
print("Pass" if islandPerimeter(grid) == ans else "Fail")
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:
grid = [[1]]
ans = 4
print("Pass" if islandPerimeter(grid) == ans else "Fail")
# Example 3:
grid = [[1, 0]]
ans = 4
print("Pass" if islandPerimeter(grid) == ans else "Fail")
# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
