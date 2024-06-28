# 452. Minimum Number of Arrows to Burst Balloons
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically ( in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# Input: array of intervals
# Ouput: count of overlaps
# My Solution: merge intervals, and return number of merged intervals
def findMinArrowShots(points):
    points.sort()
    interval = points[0]
    ans = []
    for start, end in points[1:]:
        if interval[0] > end:
            ans.append([start, end])
        elif interval[1] < start:
            ans.append(interval)
            interval = [start, end]
        else:
            new_start = max(start, interval[0])
            new_end = min(end, interval[1])
            interval = [new_start, new_end]
    ans.append(interval)

    return len(ans)


# Example 1:
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
ans = 2
print("Pass" if findMinArrowShots(points) == ans else "Fail")
# Example 2:
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
ans = 4
print("Pass" if findMinArrowShots(points) == ans else "Fail")
# Example 3:
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
ans = 2
print("Pass" if findMinArrowShots(points) == ans else "Fail")
# Example 4:
points = [[3, 9], [7, 12], [3, 8], [6, 8], [
    9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
ans = 2
print("Pass" if findMinArrowShots(points) == ans else "Fail")

# OTHER SOLUTIONS:


def countArrowShots(points):
    points.sort()
    res = len(points)
    prev = points[0]
    for start, end in points[1:]:
        if start <= prev[1]:
            res -= 1
            prev = [start, min(end, prev[1])]
        else:
            prev = [start, end]
    return res


# Example 1:
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
ans = 2
print("Pass" if countArrowShots(points) == ans else "Fail")
# Example 2:
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
ans = 4
print("Pass" if countArrowShots(points) == ans else "Fail")
# Example 3:
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
ans = 2
print("Pass" if countArrowShots(points) == ans else "Fail")
# Example 4:
points = [[3, 9], [7, 12], [3, 8], [6, 8], [
    9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
ans = 2
print("Pass" if countArrowShots(points) == ans else "Fail")
# Explanation: The balloons can be burst by 2 arrows:


def countArrowsShotByEnd(points):
    points.sort(key=lambda x: x[-1])
    count = 1
    last_end = points[0][1]
    for start, end in points[1:]:
        if start > last_end:
            count += 1
            last_end = end
    return count


# Example 1:
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
ans = 2
print("Pass" if countArrowsShotByEnd(points) == ans else "Fail")
# Example 2:
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
ans = 4
print("Pass" if countArrowsShotByEnd(points) == ans else "Fail")
# Example 3:
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
ans = 2
print("Pass" if countArrowsShotByEnd(points) == ans else "Fail")
# Example 4:
points = [[3, 9], [7, 12], [3, 8], [6, 8], [
    9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
ans = 2
print("Pass" if countArrowsShotByEnd(points) == ans else "Fail")
