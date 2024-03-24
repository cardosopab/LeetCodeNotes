# 57. Insert Interval
# Medium
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

def insert(intervals, newInterval):
    curr = newInterval
    ans = []
    for start, end in intervals:
        curr_start, curr_end = curr[0], curr[1]
        # Insert [start, end]
        if end < curr_start:
            ans.append([start, end])

        # Insert curr
        elif start > curr_end:
            ans.append(curr)
            curr = [start, end]

        # Update newInterval
        else:
            new_start = min(start, curr_start)
            new_end = max(end, curr_end)
            curr = [new_start, new_end]
    ans.append(curr)
    return ans


# Example 1:
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
ans = [[1, 5], [6, 9]]
print("Pass" if insert(intervals, newInterval) == ans else "Fail")
# Example 2:
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
ans = [[1, 2], [3, 10], [12, 16]]
print("Pass" if insert(intervals, newInterval) == ans else "Fail")
