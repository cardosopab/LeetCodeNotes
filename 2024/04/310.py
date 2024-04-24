# 310. Minimum Height Trees
# Medium
# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


from typing import List
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        levels = []
        layers = [0] * n
        graph = defaultdict(list)

        for x, y in edges:
            layers[x] += 1
            layers[y] += 1
            graph[x].append(y)
            graph[y].append(x)

        for i, layer in enumerate(layers):
            if layer == 1:
                levels.append(i)

        while True:
            nxt = []

            for level in levels:
                for child in graph[level]:
                    layers[child] -= 1
                    if layers[child] == 1:
                        nxt.append(child)

            if not nxt:
                return levels

            levels = nxt


# Example 1:
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
ans = [1]
res = Solution().findMinHeightTrees(n, edges)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# Example 2:
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
ans = [3, 4]
res = Solution().findMinHeightTrees(n, edges)
print(res)
print("Pass" if res == ans else "Fail")

# Constraints:
# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        levels = {}
        q = deque()

        for src, nei in graph.items():
            if len(nei) == 1:
                q.append(src)
            levels[src] = len(nei)

        while q:
            if n <= 2:
                return list(q)
            for i in range(len(q)):
                node = q.popleft()
                n -= 1
                for edge in graph[node]:
                    levels[edge] -= 1
                    if levels[edge] == 1:
                        q.append(edge)


# Example 1:
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
ans = [1]
res = Solution().findMinHeightTrees(n, edges)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# Example 2:
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
ans = [3, 4]
res = Solution().findMinHeightTrees(n, edges)
print(res)
print("Pass" if res == ans else "Fail")


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        q = []
        degrees = [float("inf")] * n

        for i in range(n):
            degrees[i] = len(graph[i])
            if degrees[i] == 1:
                q.append(i)
                degrees[i] -= 1

        while True:
            ans = q[:]
            q2 = []
            for node in q:
                for v in graph[node]:
                    if degrees[v] > 0:
                        degrees[v] -= 1
                        if degrees[v] == 1:
                            q2.append(v)
            if len(q2) == 0:
                return ans
            q = q2


# Example 1:
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
ans = [1]
res = Solution().findMinHeightTrees(n, edges)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# Example 2:
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
ans = [3, 4]
res = Solution().findMinHeightTrees(n, edges)
print(res)
print("Pass" if res == ans else "Fail")
