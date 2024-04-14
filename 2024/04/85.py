# 85. Maximal Rectangle
# Hard
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.


def maximalRectangle(matrix):
    R = len(matrix)
    C = len(matrix[0])

    cols = [[0] * (C + 1) for _ in range(R + 1)]

    for x in range(R):
        for y in range(C):
            cols[x + 1][y] = cols[x][y] + int(matrix[x][y])

    def all_ones(top, bot, y):
        return cols[bot + 1][y] - cols[top][y] == bot - top + 1

    best = 0

    for top in range(R):
        for bot in range(top, R):
            curr = 0

            for y in range(C):
                if all_ones(top, bot, y):
                    curr += 1
                else:
                    curr = 0

                best = max(best, curr * (bot - top + 1))

    return best


# Example 1:
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
ans = 6
print("Pass" if maximalRectangle(matrix) == ans else "Fail")
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:
matrix = [["0"]]
ans = 0
print("Pass" if maximalRectangle(matrix) == ans else "Fail")
# Example 3:
matrix = [["1"]]
ans = 1
print("Pass" if maximalRectangle(matrix) == ans else "Fail")
# Constraints:
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
