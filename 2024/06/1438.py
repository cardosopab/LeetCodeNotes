# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Medium
# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

from collections import deque
from typing import List
 
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        left = ans = 0

        for right, n in enumerate(nums):
            while max_q and max_q[-1] < n:
                max_q.pop()
            max_q.append(n)

            while min_q and min_q[-1] > n:
                min_q.pop()
            min_q.append(n)

            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[left]:
                    max_q.popleft()
                if min_q[0] == nums[left]:
                    min_q.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans

# Example 1:
nums = [8,2,4,7]
limit = 4
ans = 2 
res = Solution().longestSubarray(nums, limit)
print("Pass" if ans == res else "False")
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.

# Example 2:
nums = [10,1,2,4,7,2]
limit = 5
ans = 4 
res = Solution().longestSubarray(nums, limit)
print("Pass" if ans == res else "False")
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

# Example 3:
nums = [4,2,2,2,4,4,2,2]
limit = 0
ans = 3
res = Solution().longestSubarray(nums, limit)
print("Pass" if ans == res else "False")

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= limit <= 109
