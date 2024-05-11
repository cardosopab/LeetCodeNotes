# 786. K-th Smallest Prime Fraction
# Medium
# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].


import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        N = len(arr)
        heap = []

        for i in range(N):
            for j in range(i, N):
                heapq.heappush(heap, [arr[i]/arr[j], [arr[i], arr[j]]])

        while k:
            _, pair = heapq.heappop(heap)
            k -= 1

        return pair


# Example 1:
arr = [1, 2, 3, 5]
k = 3
ans = [2, 5]
res = Solution().kthSmallestPrimeFraction(arr, k)
print("Pass" if res == ans else f"Fail: {res}")
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.

# Example 2:
arr = [1, 7]
k = 1
ans = [1, 7]
res = Solution().kthSmallestPrimeFraction(arr, k)
print("Pass" if res == ans else f"Fail: {res}")


# Constraints:
# 2 <= arr.length <= 1000
# 1 <= arr[i] <= 3 * 104
# arr[0] == 1
# arr[i] is a prime number for i > 0.
# All the numbers of arr are unique and sorted in strictly increasing order.
# 1 <= k <= arr.length * (arr.length - 1) / 2
