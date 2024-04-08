# 1544. Make The String Great
# Easy
# Given a string s of lower and upper case English letters.
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
# Notice that an empty string is also good.
def makeGood(s):
    def charCompare(x, y):
        if x.lower() == y.lower() and (
                x.isupper() and y.islower() or x.islower() and y.isupper()
        ):
            return True
        return False
    res = []
    for i in range(len(s)):
        if len(res) > 0 and charCompare(res[-1], s[i]):
            res.pop()
        else:
            res.append(s[i])
    return "".join(res)


# Example 1:
s = "leEeetcode"
ans = "leetcode"
print("Pass" if makeGood(s) == ans else "Fail")
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
# Example 2:
s = "abBAcC"
ans = ""
print("Pass" if makeGood(s) == ans else "Fail")
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# Example 3:
s = "s"
ans = "s"
print("Pass" if makeGood(s) == ans else "Fail")
# Example 4:
s = "RLlr"
ans = ""
print("Pass" if makeGood(s) == ans else "Fail")
# Example 5:
s = "mC"
ans = "mC"
print("Pass" if makeGood(s) == ans else "Fail")
