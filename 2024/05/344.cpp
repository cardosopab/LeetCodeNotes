// 344. Reverse String
// Solved
// Easy
// Write a function that reverses a string. The input string is given as an
// array of characters s.

// You must do this by modifying the input array in-place with O(1) extra
// memory.

#include <iostream>
#include <vector>

class Solution {
public:
  virtual void reverseString(std::vector<char> &s) = 0;
};

class Solution1 : public Solution {
public:
  void reverseString(std::vector<char> &s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
      char temp = s[left];
      s[left] = s[right];
      s[right] = temp;
      left++;
      right--;
    }
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<char> s1 = {'h', 'e', 'l', 'l', 'o'};
  std::vector<char> ans1 = {'o', 'l', 'l', 'e', 'h'};
  sol->reverseString(s1);
  std::cout << (s1 == ans1 ? "Pass" : "Fail") << std::endl;

  // Example 2:
  std::vector<char> s2 = {'H', 'a', 'n', 'n', 'a', 'h'};
  std::vector<char> ans2 = {'h', 'a', 'n', 'n', 'a', 'H'};
  sol->reverseString(s2);
  std::cout << (s2 == ans2 ? "Pass" : "Fail") << std::endl;

  // Constraints:
  // 1 <= s.length <= 105
  // s[i] is a printable ascii character.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
