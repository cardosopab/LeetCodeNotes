# 752. Open the Lock
# Medium
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
#
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
#

from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        origin = "0000"
        ends = set(deadends)

        if origin in ends or target in ends:
            return -1

        q = deque([origin])
        best = {origin: 0}

        while q:
            node = q.popleft()

            if node == target:
                return best[node]

            for i in range(4):
                for d in [1, -1]:
                    curr = int(node[i])
                    curr += d
                    curr %= 10

                    nxt = node[:i] + str(curr) + node[i + 1 :]

                    if nxt in ends:
                        continue
                    if nxt in best:
                        continue
                    if nxt == target:
                        return best[node] + 1

                    best[nxt] = best[node] + 1
                    q.append(nxt)

        return -1


# Example 1:
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
ans = 6
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

# Example 2:
deadends = ["8888"]
target = "0009"
ans = 1
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

# Example 3:
deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"
ans = -1
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation: We cannot reach the target without getting stuck.

# Constraints:
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.


class Pair:
    def __init__(self, comb: str, moves: int):
        self.comb = comb
        self.moves = moves


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        visited = set(deadends)
        q = deque([Pair(start, 0)])

        if start in visited:
            return -1

        visited.add(start)

        while q:
            item = q.popleft()
            if item.comb == target:
                return item.moves
            for child in self.combinations(item.comb):
                if child not in visited:
                    visited.add(child)
                    q.append(Pair(child, item.moves + 1))
        return -1

    def combinations(self, comb):
        res = []
        for i in range(4):
            for j in [1, -1]:
                curr = int(comb[i])
                curr += j
                curr %= 10

                nxt = comb[:i] + str(curr) + comb[i + 1 :]
                res.append(nxt)
        return res


# Example 1:
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
ans = 6
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

# Example 2:
deadends = ["8888"]
target = "0009"
ans = 1
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

# Example 3:
deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"
ans = -1
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation: We cannot reach the target without getting stuck.


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        visited = set(deadends)
        q = deque([(start, 0)])

        if start in visited:
            return -1

        visited.add(start)

        while q:
            item = q.popleft()
            if item[0] == target:
                return item[1]
            for child in self.combinations(item[0]):
                if child not in visited:
                    visited.add(child)
                    q.append((child, item[1] + 1))
        return -1

    def combinations(self, comb):
        res = []
        for i in range(4):
            for j in [1, -1]:
                curr = int(comb[i])
                curr += j
                curr %= 10

                nxt = comb[:i] + str(curr) + comb[i + 1 :]
                res.append(nxt)
        return res


# Example 1:
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
ans = 6
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

# Example 2:
deadends = ["8888"]
target = "0009"
ans = 1
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

# Example 3:
deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"
ans = -1
res = Solution().openLock(deadends, target)
# print(res)
print("Pass" if res == ans else "Fail")
# Explanation: We cannot reach the target without getting stuck.
