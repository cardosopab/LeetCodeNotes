# 834. Sum of Distances in Tree
# Hard
# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

from typing import List
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        counts = [0] * n
        distances = [0] * n
        tree = defaultdict(list)

        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)

        def getCounts(node, parent):
            dist = 0
            for child in tree[node]:
                if child != parent:
                    dist += getCounts(child, node) + counts[child]
                    counts[node] += counts[child]

            counts[node] += 1
            return dist

        distances[0] = getCounts(0, -1)

        def getDistances(node, parent):
            for child in tree[node]:
                if child != parent:
                    distances[child] = distances[node] - \
                        counts[child] + (n - counts[child])
                    getDistances(child, node)

        getDistances(0, -1)
        return distances


# Example 1:
n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
ans = [8, 12, 6, 10, 10, 10]
res = Solution().sumOfDistancesInTree(n, edges)
print(res)
print("Pass" if res == ans else "Fail")
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.

# Example 2:
n = 1
edges = []
ans = [0]
res = Solution().sumOfDistancesInTree(n, edges)
print(res)
print("Pass" if res == ans else "Fail")

# Example 3:
n = 2
edges = [[1, 0]]
ans = [1, 1]
res = Solution().sumOfDistancesInTree(n, edges)
print(res)
print("Pass" if res == ans else "Fail")

# Constraints:
# 1 <= n <= 3 * 104
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.
