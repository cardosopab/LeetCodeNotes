// 1408. String Matching in an Array
// Easy
// Topics
// Companies
// Hint
// Given an array of string words, return all strings in words that is a
// substring of another word. You can return the answer in any order.
//
// A substring is a contiguous sequence of characters within a string
//

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
class Solution {
public:
  std::vector<std::string> stringMatching(std::vector<std::string> words) {
    std::vector<std::string> res;
    std::unordered_set<std::string> set;
    int N = words.size();

    for (auto w : words) {
      for (auto x : words) {
        if (w != x && x.find(w) != std::string::npos)
          set.emplace(w);
      }
    }
    for (auto w : set)
      res.push_back(w);
    return res;
  }
};
bool equal_vectors(std::vector<std::string> &arr1,
                   std::vector<std::string> &arr2) {
  if (arr1.size() == arr2.size()) {
    for (auto w : arr1) {
      if (std::find(arr2.begin(), arr2.end(), w) == arr2.end()) {
        return false;
      }
    }
  } else
    return false;
  return true;
}

int main() {
  // Example 1:
  std::vector<std::string> words = {"mass", "as", "hero", "superhero"};
  std::vector<std::string> ans = {"as", "hero"};
  std::vector<std::string> temp = Solution().stringMatching(words);
  std::cout << (equal_vectors(ans, temp) ? "Pass" : "Fail") << std::endl;
  // Explanation: "as" is substring of "mass" and "hero" is substring of
  // "superhero".
  // {"hero","as"} is also a valid answer.

  // Example 2:
  words = {"leetcode", "et", "et", "code"};
  ans = {"et", "code"};
  temp = Solution().stringMatching(words);
  std::cout << (equal_vectors(ans, temp) ? "Pass" : "Fail") << std::endl;
  // Explanation: "et", "code" are substring of "leetcode".

  // Example 3:
  words = {"blue", "green", "bu"};
  ans = {};
  temp = Solution().stringMatching(words);
  std::cout << (equal_vectors(ans, temp) ? "Pass" : "Fail") << std::endl;
  // Explanation: No string of words is substring of another string.
  //
  //
  // Constraints:
  //
  // 1 <= words.length <= 100
  // 1 <= words{i}.length <= 30
  // words{i} contains only lowercase English letters.
  // All the strings of words are unique.
}
