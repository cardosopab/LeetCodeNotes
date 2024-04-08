# Code
# 1249. Minimum Remove to Make Valid Parentheses
# Medium
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the ansulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.


def minRemoveToMakeValid(s):
    remove, ans, stack = set(), [], []

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        if c == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                remove.add(i)

    remove.update(stack)
    for i, c in enumerate(s):
        if i not in remove:
            ans.append(c)

    ans = "".join(ans)
    # print(ans)
    return ans


# Example 1:
s = "lee(t(c)o)de)"
ans = "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")
# Example 2:
s = "a)b(c)d"
ans = "ab(c)d"
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")
# Example 3:
s = "))(("
ans = ""
# Explanation: An empty string is also valid.
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")


def minRemoveToMakeValid(s):
    closed, total, ans = 0, 0, []

    for c in s:
        if c == ")":
            closed += 1

    for c in s:
        if c == ")":
            closed -= 1
            if total > 0:
                ans.append(")")
                total -= 1
        elif c == "(":
            if total + 1 <= closed:
                ans.append("(")
                total += 1
        else:
            ans.append(c)

    return "".join(ans)


# Example 1:
s = "lee(t(c)o)de)"
ans = "lee(t(c)o)de"
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
s = "a)b(c)d"
ans = "ab(c)d"
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")
# Example 3:
s = "))(("
ans = ""
# Explanation: An empty string is also valid.
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")


def minRemoveToMakeValid(s):
    ans = []
    # Extras parentheses
    count = 0

    for c in s:
        if c == "(":
            ans.append(c)
            count += 1
        elif c == ")" and count > 0:
            ans.append(c)
            count -= 1
        elif c != ")":
            ans.append(c)

    filtered = []
    for c in ans[::-1]:
        if c == "(" and count > 0:
            count -= 1
        else:
            filtered.append(c)
    return "".join(filtered[::-1])


# Example 1:
s = "lee(t(c)o)de)"
ans = "lee(t(c)o)de"
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
s = "a)b(c)d"
ans = "ab(c)d"
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")
# Example 3:
s = "))(("
ans = ""
# Explanation: An empty string is also valid.
print("Pass" if minRemoveToMakeValid(s) == ans else "Fail")
