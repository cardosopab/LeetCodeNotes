# 402. Remove K Digits
# Medium
# Topics
# Companies
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.


from collections import deque


def removeKDigits(nums, k):
    stack = deque()

    for n in num:
        while len(stack) > 0 and stack[-1] > n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    while len(stack) > 1 and stack[0] == "0":
        stack.popleft()

    while k > 0 and len(stack) > 0:
        stack.pop()
        k -= 1

    ans = "".join(stack)
    return ans if ans != "" else "0"


# Example 1:
num = "1432219"
k = 3
ans = "1219"
print("Pass" if removeKDigits(num, k) == ans else "Fail")
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""
[1
"""
# Example 2:
num = "10200"
k = 1
ans = "200"
print("Pass" if removeKDigits(num, k) == ans else "Fail")
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:
num = "10"
k = 2
ans = "0"
print("Pass" if removeKDigits(num, k) == ans else "Fail")
# Example 4:
num = "12345"
k = 2
ans = "123"
print("Pass" if removeKDigits(num, k) == ans else "Fail")
# Example 5:
num = "9"
k = 1
ans = "0"
print("Pass" if removeKDigits(num, k) == ans else "Fail")
# Example 6:
num = "10001"
k = 4
ans = "0"
print("Pass" if removeKDigits(num, k) == ans else "Fail")
# Example 7:
num = "1234567890"
k = 9
ans = "0"
print("Pass" if removeKDigits(num, k) == ans else "Fail")
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
# Constraints:
# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
