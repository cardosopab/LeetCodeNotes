// 726. Number of Atoms
// Hard
// Given a string formula representing a chemical formula, return the count of
// each atom.

// The atomic element always starts with an uppercase character, then zero or
// more lowercase letters, representing the name.

// One or more digits representing that element's count may follow if the count
// is greater than 1. If the count is 1, no digits will follow.

// For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
// Two formulas are concatenated together to produce another formula.

// For example, "H2O2He3Mg4" is also a formula.
// A formula placed in parentheses, and a count (optionally added) is also a
// formula.

// For example, "(H2O2)" and "(H2O2)3" are formulas.
// Return the count of all elements as a string in the following form: the first
// name (in sorted order), followed by its count (if that count is more than 1),
// followed by the second name (in sorted order), followed by its count (if that
// count is more than 1), and so on.

// The test cases are generated so that all the values in the output fit in a
// 32-bit integer.

#include <cctype>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
class Solution {
public:
  virtual std::string countOfAtoms(std::string formula) = 0;
};

class Solution1 : public Solution {
public:
  std::pair<int, int> get_count(const std::string &formula, int j) {
    int n = 0;
    while (j < formula.size() && std::isdigit(formula[j])) {
      n = n * 10 + (formula[j] - '0');
      j++;
    }
    return std::make_pair(j, n == 0 ? 1 : n);
  };
  std::string countOfAtoms(std::string formula) {
    int N = formula.size();
    std::vector<std::map<std::string, int>> stack(1);
    for (int i = 0; i < N; i++) {
      if (formula[i] == '(') {
        stack.emplace_back();
      } else if (formula[i] == ')') {
        auto [j, x] = get_count(formula, i + 1);
        auto top = stack.back();
        stack.pop_back();
        for (auto &[el, cnt] : top) {
          stack.back()[el] += cnt * x;
        }
        i = j - 1;
      } else {
        int j = i + 1;
        while (j < N && std::islower(formula[j])) {
          j++;
        }
        std::string el = formula.substr(i, j - i);
        auto [k, x] = get_count(formula, j);
        i = k - 1;
        stack.back()[el] += x;
      }
    }
    std::string res = "";
    for (auto &r : stack) {
      for (auto &[el, cnt] : r) {
        res += el + (cnt > 1 ? std::to_string(cnt) : "");
      }
    }
    return res;
  }
};

/*
{K:4, N:2, O:12, S:2}
*/

void test_solution(Solution *sol) {
  // Example 1:
  std::string formula = "H2O";
  std::string ans = "H2O";
  std::string res = sol->countOfAtoms(formula);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The count of elements are {'H': 2, 'O': 1}.

  // Example 2:
  formula = "Mg(OH)2";
  ans = "H2MgO2";
  res = sol->countOfAtoms(formula);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

  // Example 3:
  formula = "K4(ON(SO3)2)2";
  ans = "K4N2O14S4";
  res = sol->countOfAtoms(formula);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

  // Constraints:
  // 1 <= formula.length <= 1000
  // formula consists of English letters, digits, '(', and ')'.
  // formula is always valid.
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
