# 592. Fraction Addition and Subtraction
# Medium
# Topics
# Companies
# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.


class Solution:
    def fractionAddition(self, expression):
        i, N, frac = 0, len(expression), []

        while i < N:
            start = i

            if expression[i] == "+" or expression[i] == "-":
                i += 1
            while i < N and (expression[i] != "+" and expression[i] != "-"):
                i += 1

            e = expression[start:i]
            if e == "":
                continue

            frac.append([int(x) for x in e.split("/")])

        prev = frac[0]
        for i in range(1, len(frac)):
            curr_num, curr_den = frac[i][0], frac[i][1]

            if prev[1] != curr_den:
                new_num, new_den = (
                    prev[0] * curr_den + curr_num * prev[1],
                    prev[1] * curr_den,
                )
            else:
                new_num, new_den = prev[0] + curr_num, prev[1]

            prev = [new_num, new_den]

        if prev[0] == 0:
            return "0/1"

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        if abs(prev[0]) > 1:
            div = gcd(max(prev[0], prev[1]), min(prev[0], prev[1]))
            prev[0], prev[1] = prev[0] // div, prev[1] // div

        if prev[1] < 0:
            prev[0] *= -1
            prev[1] *= -1

        return f"{prev[0]}/{prev[1]}"


# Example 1:
expression = "-1/2+1/2"
ans = "0/1"
res = Solution().fractionAddition(expression)
print("Pass" if ans == res else "Fail")

# Example 2:
expression = "-1/2+1/2+1/3"
ans = "1/3"
res = Solution().fractionAddition(expression)
print("Pass" if ans == res else "Fail")

# Example 3:
expression = "1/3-1/2"
ans = "-1/6"
res = Solution().fractionAddition(expression)
print("Pass" if ans == res else "Fail")

# Example 4:
expression = "7/2+2/3-3/4"
ans = "41/12"
res = Solution().fractionAddition(expression)
print("Pass" if ans == res else "Fail")

# Example 5:
expression = "-4/7-3/4+2/3"
ans = "-55/84"
res = Solution().fractionAddition(expression)
print("Pass" if ans == res else "Fail")

# Constraints:
# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1, 10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
