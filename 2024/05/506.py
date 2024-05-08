# 506. Relative Ranks
# Easy
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
#
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
#
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
def findRelativeRanks(score):
    ans = []
    sort = sorted(score, reverse=True)
    ranks = [
        "Gold Medal",
        "Silver Medal",
        "Bronze Medal",
    ]

    for s in score:
        idx = sort.index(s)
        if idx < 3:
            ans.append(ranks[idx])
        else:
            ans.append(str(idx + 1))

    return ans


# Example 1:
score = [5, 4, 3, 2, 1]
ans = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
res = findRelativeRanks(score)
print("Pass" if res == ans else f"Fail {res}")
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

# Example 2:
score = [10, 3, 8, 9, 4]
ans = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
res = findRelativeRanks(score)
print("Pass" if res == ans else f"Fail {res}")
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

# Example 3:
score = [1]
ans = ["Gold Medal"]
res = findRelativeRanks(score)
print("Pass" if res == ans else f"Fail {res}")

# Constraints:
# n == score.length
# 1 <= n <= 104
# 0 <= score[i] <= 106
# All the values in score are unique.
