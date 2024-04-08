# 678. Valid Parenthesis String
# Medium
# Topics
# Companies
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


def checkValidString(s):
    open, wild = [], []

    # Append ( indexis into open array
    # Append * indexis into wild array
    # Else pop open if not empty, elif pop wild else return False
    for i, c in enumerate(s):
        if c == "(":
            open.append(i)
        elif c == "*":
            wild.append(i)
        else:
            if open:
                open.pop()
            elif wild:
                wild.pop()
            else:
                return False

    # While open is not empty
    # Pop open and wild
    # Return False if wild is empty or last open > last wild
    while open:
        if not wild or (wild[-1] < open[-1]):
            return False
        open.pop()
        wild.pop()

    return True


# Example 1:
s = "()"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
# Example 2:
s = "(*)"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
# Example 3:
s = "(*))"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
# Constraints:
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.


def checkValidString(s):
    N = len(s)

    has_cache = [[False] * (N + 1) for _ in range(N + 1)]
    cache = [[None] * (N + 1) for _ in range(N + 1)]

    # index => 0 to N => the number of characters we've processed
    # depth => 0 to N => the depth of parentheses we've processed
    def go(i, depth):
        if i == N:
            if depth == 0:
                return True
            return False

        if has_cache[i][depth]:
            return cache[i][depth]

        has_cache[i][depth] = True

        if s[i] == "(":
            cache[i][depth] = go(i + 1, depth + 1)
            return cache[i][depth]
        elif s[i] == ")":
            if depth - 1 >= 0:
                cache[i][depth] = go(i + 1, depth - 1)
                return cache[i][depth]
            else:
                cache[i][depth] = False
                return cache[i][depth]
        else:
            # s[i] == "*"
            cache[i][depth] = (
                go(i + 1, depth + 1)
                or (depth - 1 >= 0 and go(i + 1, depth - 1))
                or go(i + 1, depth)
            )
        return cache[i][depth]

    return go(0, 0)


# Example 1:
s = "()"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
# Example 2:
s = "(*)"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
# Example 3:
s = "(*))"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")


def checkValidString(s):
    possible = set([0])

    for c in s:
        next_possible = set()

        if c == "(":
            for p in possible:
                next_possible.add(p + 1)

        elif c == ")":
            for p in possible:
                if p - 1 >= 0:
                    next_possible.add(p - 1)

        else:
            for p in possible:
                next_possible.add(p + 1)
                if p - 1 >= 0:
                    next_possible.add(p - 1)
                next_possible.add(p)
        possible = next_possible
        # print(possible)

    return 0 in possible


# Example 1:
s = "()"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
# Example 2:
s = "(*)"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
# Example 3:
s = "(*))"
ans = True
print("Pass" if checkValidString(s) == ans else "Fail")
