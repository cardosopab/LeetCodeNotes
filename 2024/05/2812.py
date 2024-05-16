# 2812. Find the Safest Path in a Grid
# Medium
# You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
# 
# A cell containing a thief if grid[r][c] = 1
# An empty cell if grid[r][c] = 0
# You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.
# 
# The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.
# 
# Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
# 
# An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.
# 
# The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
 
  
from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid):
        N = len(grid)
        # Get the safety numbers
        safety=[[float("inf")]*N for _ in range(N)]
        dirs = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1),
        ]

        # "regular" BFS - multi-source shortest Manhattan distance path from the thief
        q = deque()

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    safety[i][j] = 0
                    q.append((0,i,j))
        while q:
            d, x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and safety[nx][ny] == float("inf"):
                    safety[nx][ny] = d + 1
                    q.append((d+1, nx,ny))

        # 0-1 BFS
        visited = [[False]*N for _ in range(N)]
        q = deque()
        q.append((safety[0][0], 0, 0))
        visited[0][0] = True

        while q:
            d, x, y = q.popleft()

            if x == N - 1 and y == N - 1:
                return d

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if d <= safety[nx][ny]:
                        q.appendleft((d, nx,ny))
                    else:
                        q.append((safety[nx][ny], nx,ny))
        return -1


# Example 1:
grid = [[1,0,0],[0,0,0],[0,0,1]]
ans = 0
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")
# Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

# Example 2:
grid = [[0,0,1],[0,0,0],[0,0,0]]
ans = 2
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.

# Example 3:
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
ans = 2
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
# - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.

# Constraints:
# 1 <= grid.length == n <= 400
# grid[i].length == n
# grid[i][j] is either 0 or 1.
# There is at least one thief in the grid.


class Solution:
    def maximumSafenessFactor(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        N = len(grid)

        dq = deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dq.append((r, c, 1))

        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1)) 
        while dq:
            r, c, depth = dq.popleft()
            depth += 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    grid[nr][nc] = depth
                    dq.append((nr, nc, depth))

        ans = -grid[0][0]
        heap = [(-grid[0][0], 0, 0)]
        heapq.heapify(heap)
        while heap:
            val, r, c = heapq.heappop(heap)
            if r == c == N-1:
                break
            ans = max(val, ans)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0:
                    heapq.heappush(heap, (-grid[nr][nc], nr, nc))
                    grid[nr][nc] = -1

        return -ans -1


# Example 1:
grid = [[1,0,0],[0,0,0],[0,0,1]]
ans = 0
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")

# Example 2:
grid = [[0,0,1],[0,0,0],[0,0,0]]
ans = 2
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")

# Example 3:
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
ans = 2
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")


class Solution:
    def maximumSafenessFactor(self, grid):
        N = len(grid)
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1)) 

        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        def precompute():
            q = deque()
            min_dist = {}

            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append((r, c, 0))
                        min_dist[(r, c)] = 0

            while q:
                r, c, dist = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if in_bounds(nr, nc) and (nr, nc) not in min_dist:
                        min_dist[(nr, nc)] = dist + 1
                        q.append((nr, nc, dist + 1))
            return min_dist

        min_dist = precompute()
        heap = [(-min_dist[(0,0)], 0, 0)] # (dist, r, c)
        visit = set()
        visit.add((0,0))
        while heap:
            dist, r, c = heapq.heappop(heap)
            dist = -dist
            if (r, c) == (N-1, N-1):
                return dist
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    dist2 = min(dist, min_dist[(nr, nc)])
                    heapq.heappush(heap, (-dist2, nr, nc))


# Example 1:
grid = [[1,0,0],[0,0,0],[0,0,1]]
ans = 0
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")

# Example 2:
grid = [[0,0,1],[0,0,0],[0,0,0]]
ans = 2
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")

# Example 3:
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
ans = 2
res = Solution().maximumSafenessFactor(grid)
print("Pass" if res == ans else f"Fail {res}")
