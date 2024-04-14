# 221. Maximal Square
# Medium
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


def maximalSquare(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    cache = {}

    def helper(r, c):
        if r >= ROWS or c >= COLS:
            return 0

        if (r, c) not in cache:
            down = helper(r + 1, c)
            right = helper(r, c + 1)
            diag = helper(r + 1, c + 1)

            cache[(r, c)] = 0
            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, right, diag)

        return cache[(r, c)]

    helper(0, 0)
    ans = max(cache.values()) ** 2
    print(ans)
    return ans


# Example 1:
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
ans = 4
print("Pass" if maximalSquare(matrix) == ans else "Fail")
# Example 2:
matrix = [["0", "1"], ["1", "0"]]
ans = 1
print("Pass" if maximalSquare(matrix) == ans else "Fail")
# Example 3:
matrix = [["0"]]
ans = 0
print("Pass" if maximalSquare(matrix) == ans else "Fail")
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
