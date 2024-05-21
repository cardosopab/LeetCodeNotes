# 78. Subsets
# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


class Solution:
    def subsets(self, nums):
        N = len(nums)
        ans = []

        def dfs(i, curr):
            if i == N:
                ans.append(curr[:])
                return
            
            dfs(i + 1, curr)

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

        dfs(0, [])
        return ans

# Example 1:
nums = [1, 2, 3]
# ans = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# NOTE: unordered solution also passes
ans = [[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3]]
res = Solution().subsets(nums)
print("Pass" if ans == res else f"Fail: {res}")

# Example 2:
nums = [0]
ans = [[], [0]]
res = Solution().subsets(nums)
print("Pass" if ans == res else f"Fail: {res}")

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


class Solution:
    def subsets(self, nums):
        ans = [[]]

        for n in nums:
            ans += [prev + [n] for prev in ans]
        return ans

# Example 1:
nums = [1, 2, 3]
ans = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
res = Solution().subsets(nums)
print("Pass" if ans == res else f"Fail: {res}")

# Example 2:
nums = [0]
ans = [[], [0]]
res = Solution().subsets(nums)
print("Pass" if ans == res else f"Fail: {res}")
