# 1992. Find All Groups of Farmland
# Medium
# You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.
#
# To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.
#
# land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].
#
# Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.


"""
m x n matrix of 0s and 1s

find top left and bottom right
[r1, c1, r2, c2]
of each 1s rectangle

dfs with a visited matrix

how do I know which is the top left, and bottom right corner?
recurse until found?
top left == min((r,c))
bottom rigth == max((r,c))

add array of [r1, c1, r2, c2] into result array
return result array
"""


def findFarmLand(land):
    R, C, res = len(land), len(land[0]), []
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    visited = [[False] * C for _ in range(R)]
    min_corner = (0, 0)
    max_corner = (0, 0)

    # dfs with a visited matrix
    def dfs(r, c):
        visited[r][c] = True
        for dr, dc in directions:
            xr = r + dr
            xc = c + dc
            is_greater = xr >= 0 <= xc
            is_less = xr < R and xc < C
            if is_greater and is_less and land[xr][xc] == 1 and not visited[xr][xc]:
                # how do I know which is the top left, and bottom right corner?
                # recurse until found?
                # top left == min((r,c))
                # bottom rigth == max((r,c))
                nonlocal min_corner
                nonlocal max_corner
                min_corner = min([min_corner, (xr, xc)], key=lambda x: sum(x))
                max_corner = max([max_corner, (xr, xc)], key=lambda x: sum(x))
                dfs(xr, xc)

    for r in range(R):
        for c in range(C):
            if land[r][c] == 1 and not visited[r][c]:
                min_corner = (r, c)
                max_corner = (r, c)
                dfs(r, c)
                min_r, min_c = min_corner
                max_r, max_c = max_corner
                # add array of [r1, c1, r2, c2] into result array
                res.append([min_r, min_c, max_r, max_c])

    # return result array
    return res


# Example 1:
land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
ans = [[0, 0, 0, 0], [1, 1, 2, 2]]
res = findFarmLand(land)
print(f"Pass: {res}" if res == ans else f"Fail: {res}")
# Explanation:
# The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
# The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].
# Example 2:
land = [[1, 1], [1, 1]]
ans = [[0, 0, 1, 1]]
res = findFarmLand(land)
print(f"Pass: {res}" if res == ans else f"Fail: {res}")
# Explanation:
# The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].
# Example 3:
land = [[0]]
ans = []
res = findFarmLand(land)
print(f"Pass: {res}" if res == ans else f"Fail: {res}")
# Example 4:
land = [[1, 1], [0, 0]]
ans = [[0, 0, 0, 1]]
res = findFarmLand(land)
print(f"Pass: {res}" if res == ans else f"Fail: {res}")
# Explanation:
# There are no groups of farmland.
# Constraints:
# m == land.length
# n == land[i].length
# 1 <= m, n <= 300
# land consists of only 0's and 1's.
# Groups of farmland are rectangular in shape.
