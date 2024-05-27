# 1255. Maximum Score Words Formed by Letters
# Hard
# Given a list of words, list of  single letters (might be repeating) and score of every character.
# 
# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
# 
# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.


from collections import Counter


class Solution:
    def maxScoreWords(self, words, letters, score):
        N, letter_count = len(words), Counter(letters)

        def is_valid(w, letter_count):
            word_count = Counter(w)
            return word_count <= letter_count

        def get_score(w):
            res = 0
            for c in w:
                res += score[ord(c) - ord('a')]
            return res

        def backtrack(i):
            if i == N:
                return 0

            res = backtrack(i + 1)

            nonlocal letter_count
            if is_valid(words[i], letter_count):
                word_count = Counter(words[i])
                letter_count -= word_count
                res = max(res, get_score(words[i]) + backtrack(i + 1))
                letter_count += word_count
            return res
        
        return backtrack(0)


# Example 1:
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
ans = 23
res = Solution().maxScoreWords(words, letters, score)
print("Pass" if ans == res else f"Fail: {res}")
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
# Words "dad" and "dog" only get a score of 21.

# Example 2:
words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
ans = 27
res = Solution().maxScoreWords(words, letters, score)
print("Pass" if ans == res else f"Fail: {res}")
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
# Word "xxxz" only get a score of 25.

# Example 3:
words = ["leetcode"]
letters = ["l","e","t","c","o","d"]
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
ans = 0
res = Solution().maxScoreWords(words, letters, score)
print("Pass" if ans == res else f"Fail: {res}")
# Explanation:
# Letter "e" can only be used once.

# Constraints:
# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
# words[i], letters[i] contains only lower case English letters.
