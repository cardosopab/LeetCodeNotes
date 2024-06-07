# 648. Replace Words
# Medium
# In English, we have a concept called root, which can be followed by some
# other word to form another longer word - let's call this word derivative. For
# example, when the root "help" is followed by the word "ful", we can form a
# derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of
# words separated by spaces, replace all the derivatives in the sentence with
# the root forming it. If a derivative can be replaced by more than one root,
# replace it with the root that has the shortest length.

# Return the sentence after the replacement.

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

    def search(self,word):
        ans = []
        curr = self.root
        for c in word:
            if c not in curr.children:
                return word
            ans.append(c)
            curr = curr.children[c]
            if curr.is_word:
                break
        return "".join(ans)

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        ans = sentence.split(" ")

        for w in dictionary:
            trie.insert(w)

        for i, w in enumerate(ans):
            curr = trie.search(w)
            if curr != w:
                ans[i] = curr

        return " ".join(ans)


# Example 1:
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
ans = "the cat was rat by the bat"
res = Solution().replaceWords(dictionary, sentence)
print("Pass" if res == ans else f"Fail {res}")

# Example 2:
dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
ans = "a a b c"
res = Solution().replaceWords(dictionary, sentence)
print("Pass" if res == ans else f"Fail {res}")

# Constraints:
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one
# space. sentence does not have leading or trailing spaces.

