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

class Solution1 : public Solution {
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
  Solution1 sol1;
  test_solution(&sol1);
}
