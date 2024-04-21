# 1971. Find if Path Exists in Graph
# Easy
# Topics
# Companies
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


from collections import defaultdict, deque


def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for s, d in edges:
        graph[s].append(d)
        graph[d].append(s)

    d = deque([source])
    visited = set()

    while d:
        node = d.popleft()
        visited.add(node)

        if node == destination:
            return True

        for edge in graph[node]:
            if edge not in visited:
                d.append(edge)

    return False


# Example 1:
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
res = validPath(n, edges, source, destination)
ans = True
print("Pass" if res == ans else "Fail")
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
ans = False
res = validPath(n, edges, source, destination)
print("Pass" if res == ans else "Fail")
# Explanation: There is no path from vertex 0 to vertex 5.

# Example r:
n = 10
edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
source = 5
destination = 9
ans = True
res = validPath(n, edges, source, destination)
print("Pass" if res == ans else "Fail")

# Constraints:
# 1 <= n <= 2 * 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.


def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for s, d in edges:
        graph[s].append(d)
        graph[d].append(s)
    visited = set()

    def dfs(curr, end):
        if curr == end:
            return True
        if curr in visited:
            return False

        visited.add(curr)

        for edge in graph[curr]:
            if dfs(edge, end):
                return True
        return False

    return dfs(source, destination)


# Example 1:
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
res = validPath(n, edges, source, destination)
ans = True
print("Pass" if res == ans else "Fail")
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
ans = False
res = validPath(n, edges, source, destination)
print("Pass" if res == ans else "Fail")
# Explanation: There is no path from vertex 0 to vertex 5.

# Example r:
n = 10
edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
source = 5
destination = 9
ans = True
res = validPath(n, edges, source, destination)
print("Pass" if res == ans else "Fail")
