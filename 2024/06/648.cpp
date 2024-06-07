// 648. Replace Words
// Medium
// In English, we have a concept called root, which can be followed by some
// other word to form another longer word - let's call this word derivative. For
// example, when the root "help" is followed by the word "ful", we can form a
// derivative "helpful".

// Given a dictionary consisting of many roots and a sentence consisting of
// words separated by spaces, replace all the derivatives in the sentence with
// the root forming it. If a derivative can be replaced by more than one root,
// replace it with the root that has the shortest length.

// Return the sentence after the replacement.

#include <iostream>
#include <numeric>
#include <ostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
class Solution {
public:
  virtual std::string replaceWords(std::vector<std::string> &dictionary,
                                   std::string sentence) = 0;
};

class TrieNode {
public:
  TrieNode *children[26];
  bool is_end;

  TrieNode() {
    for (int i = 0; i < 26; i++) {
      children[i] = nullptr;
    }
    is_end = false;
  }
};

class Trie {
public:
  TrieNode *root;
  Trie() { this->root = new TrieNode(); }

  void insert(std::string word) {
    TrieNode *curr = root;
    for (const char &c : word) {
      int n = int(c) - int('a');
      if (curr->children[n] == nullptr) {
        curr->children[n] = new TrieNode();
      }
      curr = curr->children[n];
    }
    curr->is_end = true;
  }

  std::string search(std::string word) {
    TrieNode *curr = root;
    std::string ans = "";
    for (const char &c : word) {
      int n = int(c) - int('a');
      if (curr->children[n] == nullptr) {
        break;
      }

      ans += char(n + int('a'));
      if (curr->children[n]->is_end) {
        return ans;
      }

      curr = curr->children[n];
    }
    return word;
  }
};

class Solution1 : public Solution {
public:
  std::string replaceWords(std::vector<std::string> &dictionary,
                           std::string sentence) {
    Trie trie = Trie();
    std::string ans = "";

    for (auto w : dictionary) {
      trie.insert(w);
    }

    for (int i = 0; i < sentence.size(); i++) {
      int j = i;
      while (j < sentence.size() && sentence[j] != ' ')
        j++;

      std::string sub_s = sentence.substr(i, j - i);
      i = j;
      std::string new_w = trie.search(sub_s);
      ans += new_w;
      if (i < sentence.size() - 1) {
        ans += ' ';
      }
    }
    return ans;
  };
};

class Solution2 : public Solution {
public:
  std::string replaceWords(std::vector<std::string> &dictionary,
                           std::string sentence) {
    // split string
    std::string temp;
    std::stringstream ss(sentence);
    std::vector<std::string> ans;
    while (std::getline(ss, temp, ' ')) {
      ans.push_back(temp);
    }

    // dic set
    std::unordered_set<std::string> dic_set;
    for (std::string w : dictionary) {
      dic_set.insert(w);
    }

    // traverse ans, and replace
    for (int i = 0; i < ans.size(); i++) {
      for (int j = 0; j < ans[i].size(); j++) {
        std::string curr = ans[i].substr(0, j);
        if (dic_set.find(curr) != dic_set.end()) {
          ans[i] = curr;
          break;
        }
      }
    }

    return std::accumulate(
        std::next(ans.begin()), ans.end(), ans[0],
        [](std::string a, std::string b) { return a + " " + b; });
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<std::string> dictionary = {"cat", "bat", "rat"};
  std::string sentence = "the cattle was rattled by the battery";
  std::string ans = "the cat was rat by the bat";
  std::string res = sol->replaceWords(dictionary, sentence);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;

  // Example 2:
  dictionary = {"a", "b", "c"};
  sentence = "aadsfasf absbs bbab cadsfafs";
  ans = "a a b c";
  res = sol->replaceWords(dictionary, sentence);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;

  // Constraints:
  // 1 <= dictionary.length <= 1000
  // 1 <= dictionary[i].length <= 100
  // dictionary[i] consists of only lower-case letters.
  // 1 <= sentence.length <= 106
  // sentence consists of only lower-case letters and spaces.
  // The number of words in sentence is in the range [1, 1000]
  // The length of each word in sentence is in the range [1, 1000]
  // Every two consecutive words in sentence will be separated by exactly one
  // space. sentence does not have leading or trailing spaces.
}

int main() {
  std::cout << "Test 1" << std::endl;
  Solution1 sol1;
  test_solution(&sol1);

  std::cout << "Test 2" << std::endl;
  Solution2 sol2;
  test_solution(&sol2);
}
