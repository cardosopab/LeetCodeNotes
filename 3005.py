# 3005. Count Elements With Maximum Frequency
# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all
#   have the maximum frequency
# The frequency of an element is the number of occurrences of that element in
#   the array

# Input nums array
# Output max frequency element count

from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums):
        count = defaultdict(int)
        maxFrequency = 0
        elementCount = 0

        for n in nums:
            # Count frequencies
            count[n] += 1
            # Update max frequency
            maxFrequency = max(maxFrequency, count[n])

        # Update element count
        for v in count.values():
            if v == maxFrequency:
                elementCount += maxFrequency

        print(elementCount)
        return elementCount


input = [1, 2, 2, 3, 1, 4]
output = 4
print("Pass" if Solution().maxFrequencyElements(input) == output else "Fail")

input = [1, 2, 3, 4, 5]
output = 5

print("Pass" if Solution().maxFrequencyElements(input) == output else "Fail")
