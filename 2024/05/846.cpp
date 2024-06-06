// 846. Hand of Straights
// Medium
// Alice has some number of cards and she wants to rearrange the cards into
// groups so that each group is of size groupSize, and consists of groupSize
// consecutive cards.

// Given an integer array hand where hand[i] is the value written on the ith
// card and an integer groupSize, return true if she can rearrange the cards, or
// false otherwise.

#include <iostream>
#include <map>
#include <vector>
class Solution {
public:
  virtual bool isNStraightHand(std::vector<int> &hand, int groupSize) = 0;
};

class Solution1 : public Solution {
public:
  bool isNStraightHand(std::vector<int> &hand, int groupSize) {
    std::map<int, int> count;
    for (int n : hand) {
      count[n]++;
    }

    while (!count.empty()) {
      auto min_key_it = count.begin();
      int start = min_key_it->first;
      for (int i = 0; i < groupSize; i++) {
        if (count.find(start) == count.end()) {
          return false;
        }
        count[start]--;
        if (count[start] == 0) {
          count.erase(start);
        }
        start++;
      }
    }
    return true;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<int> hand = {1, 2, 3, 6, 2, 3, 4, 7, 8};
  int groupSize = 3;
  bool ans = true;
  bool res = sol->isNStraightHand(hand, groupSize);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation: Alice's hand can be rearranged as {1,2,3},[2,3,4],[6,7,8]

  // Example 2:
  hand = {1, 2, 3, 4, 5};
  groupSize = 4;
  ans = false;
  res = sol->isNStraightHand(hand, groupSize);
  std::cout << (ans == res ? "Pass" : "Fail") << std::endl;
  // Explanation: Alice's hand can not be rearranged into groups of 4.

  // Constraints:
  // 1 <= hand.length <= 104
  // 0 <= hand[i] <= 109
  // 1 <= groupSize <= hand.length
  // Note: This question is the same as 1296:
  // https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
