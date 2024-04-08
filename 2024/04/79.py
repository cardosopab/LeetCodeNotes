# 79. Word Search
# Medium
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
def exist(board, word):
    R = len(board)
    C = len(board[0])
    N = len(word)

    used = [[False] * C for _ in range(R)]
    found = False

    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]

    def search(i, x, y):
        if board[x][y] != word[i]:
            return
        if i == N - 1:
            nonlocal found
            found = True
            return

        used[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and not used[nx][ny]:
                search(i + 1, nx, ny)

        used[x][y] = False

    for x in range(R):
        for y in range(C):
            search(0, x, y)

    return found


# Example 1:
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
ans = True
print("Pass" if exist(board, word) == ans else "Fail")
# Example 2:
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
ans = True
print("Pass" if exist(board, word) == ans else "Fail")
# Example 3:
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
ans = False
print("Pass" if exist(board, word) == ans else "Fail")


def exist(board, word):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = set()
    ROWS, COLS, = len(board), len(board[0])

    def dfs(row, col, i):
        if i == len(word):
            return True

        is_out_of_bounds = row < 0 or row == ROWS or col < 0 or col == COLS
        in_visited = (row, col) in visited
        if is_out_of_bounds or in_visited or board[row][col] != word[i]:
            return False

        visited.add((row, col))

        for x, y in directions:
            if dfs(row + x, col + y, i + 1):
                return True

        visited.remove((row, col))

        return False

    for row in range(ROWS):
        for col in range(COLS):
            if dfs(row, col, 0):
                return True

    return False


# Example 1:
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
ans = True
print("Pass" if exist(board, word) == ans else "Fail")
# Example 2:
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
ans = True
print("Pass" if exist(board, word) == ans else "Fail")
# Example 3:
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
ans = False
print("Pass" if exist(board, word) == ans else "Fail")

