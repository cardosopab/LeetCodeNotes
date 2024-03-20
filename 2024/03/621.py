# 621. Task Scheduler
# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
# ​Return the minimum number of intervals required to complete all tasks.
from collections import Counter


def leastInterval(tasks, n):
    counts = sorted(Counter(tasks).values(), reverse=True)
    max_val = counts[0]
    groups = max_val - 1
    items = groups * n
    for count in counts[1:]:
        items -= min(groups, count)
    idle_time = max(items, 0)
    return len(tasks) + idle_time


# Example 1:
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
ans = 8
print("Pass" if leastInterval(tasks, n) == ans else "Fail")
# Example 2:
tasks = ["A", "C", "A", "B", "D", "B"]
n = 1
ans = 6
print("Pass" if leastInterval(tasks, n) == ans else "Fail")
# Example 3:
tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
ans = 10
print("Pass" if leastInterval(tasks, n) == ans else "Fail")
