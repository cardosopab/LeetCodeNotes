# 2485. Find the Pivot Integer
# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.


# Input: integer
# Output: pivot point
# Solution: two pointer iterating to center, if match return i else -1
def pivotInteger(n):
    prefix, postfix = 0, (n * (n + 1)) // 2
    for i in range(1, n+1):
        prefix += i
        if prefix == postfix:
            return i
        elif prefix > postfix:
            break
        postfix -= i
    return -1


# Example 1:
n = 8
ans = 6
print("Pass" if pivotInteger(n) == ans else "Fail")
# Example 2:
n = 1
ans = 1
print("Pass" if pivotInteger(n) == ans else "Fail")
# Example 3:
n = 4
ans = -1
print("Pass" if pivotInteger(n) == ans else "Fail")
# Example 4:
n = 3
ans = -1
print("Pass" if pivotInteger(n) == ans else "Fail")
# Example 5:
n = 15
ans = -1
print("Pass" if pivotInteger(n) == ans else "Fail")
# Example 6:
n = 16
ans = -1
print("Pass" if pivotInteger(n) == ans else "Fail")
