# 140. Word Break II
# Hard
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s, wordDict):
        N, word_set, ans = len(s), set(wordDict), []

        def dfs(i, curr):
            if i == N:
                ans.append(" ".join(curr))
                return

            for end in range(i, N):
                curr_s = s[i:end + 1]
                if curr_s in word_set:
                    curr.append(curr_s)
                    dfs(end + 1, curr) 
                    curr.pop()
        dfs(0, [])
        return ans



# Example 1:
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
ans = ["cats and dog","cat sand dog"]
res = Solution().wordBreak(s, wordDict)
passed = True
for w in ans:
    if w not in res:
        passed = False
        break
print("Pass" if passed else f"Fail: {res}")

# Example 2:
s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
ans = ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
res = Solution().wordBreak(s, wordDict)
passed = True
for w in ans:
    if w not in res:
        passed = False
        break
print("Pass" if passed else f"Fail: {res}")
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
ans = []
res = Solution().wordBreak(s, wordDict)
passed = True
for w in ans:
    if w not in res:
        passed = False
        break
print("Pass" if passed else f"Fail: {res}")

# Constraints:
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.
