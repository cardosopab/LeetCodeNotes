# 42. Trapping Rain Water
# Hard
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


def trap(h):
    N = len(h)
    water = 0
    left_max = 0
    right_max = [0] * N

    for i in range(N - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], h[i + 1])

    for i in range(1, N):
        left_max = max(left_max, h[i - 1])
        min_wall = min(left_max, right_max[i])
        water += max(0, min_wall - h[i])

    return water


# Example 1:
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = 6
print("Pass" if trap(height) == ans else "Fail")
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
height = [4, 2, 0, 3, 2, 5]
ans = 9
print("Pass" if trap(height) == ans else "Fail")
# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


def trap(h):
    N = len(h)

    def get_prefix_max(h):
        prefix = [0]

        for i in range(N):
            prefix.append(max(h[i], prefix[-1]))
        return prefix

    left = get_prefix_max(h)
    right = get_prefix_max(h[::-1])[::-1]

    water = 0

    for i in range(N):
        water += max(min(left[i], right[i]) - h[i], 0)

    return water


# Example 1:
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = 6
print("Pass" if trap(height) == ans else "Fail")
# Example 2:
height = [4, 2, 0, 3, 2, 5]
ans = 9
print("Pass" if trap(height) == ans else "Fail")
