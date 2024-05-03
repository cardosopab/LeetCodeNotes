
// 165. Compare Version Numbers
// Medium
// Given two version numbers, version1 and version2, compare them.

// Version numbers consist of one or more revisions joined by a dot '.'. Each
// revision consists of digits and may contain leading zeros. Every revision
// contains at least one character. Revisions are 0-indexed from left to right,
// with the leftmost revision being revision 0, the next revision being revision
// 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

// To compare version numbers, compare their revisions in left-to-right order.
// Revisions are compared using their integer value ignoring any leading zeros.
// This means that revisions 1 and 001 are considered equal. If a version number
// does not specify a revision at an index, then treat the revision as 0. For
// example, version 1.0 is less than version 1.1 because their revision 0s are
// the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

// Return the following:

// If version1 < version2, return -1.
// If version1 > version2, return 1.
// Otherwise, return 0.
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

class Solution {
public:
  virtual int compareVersion(string version1, string version2) = 0;
};

class Solution1 : public Solution {
public:
  int compareVersion(string version1, string version2) {
    stringstream vstream1(version1);
    stringstream vstream2(version2);
    string token;
    vector<int> v1;
    vector<int> v2;

    while (getline(vstream1, token, '.')) {
      v1.push_back(stoi(token));
    }

    while (getline(vstream2, token, '.')) {
      v2.push_back(stoi(token));
    }

    while (v1.size() != v2.size()) {
      if (v1.size() > v2.size()) {
        v2.push_back(0);
      } else {
        v1.push_back(0);
      }
    }

    for (int i = 0; i < v1.size(); i++) {
      if (v1[i] == v2[i]) {
        continue;
      } else if (v1[i] > v2[i]) {
        return 1;
      } else {
        return -1;
      }
    }

    return 0;
  };
};

void test_solution(Solution &sol) {
  // Example 1:
  string ex1_version_a = "1.01";
  string ex1_version_b = "1.001";
  int ans1 = 0;
  int res1 = sol.compareVersion(ex1_version_a, ex1_version_b);
  cout << "Test 1" << ": " << res1 << " " << (res1 == ans1 ? "Pass" : "Fail")
       << endl;
  // Explanation: Ignoring leading zeroes, both "01" and "001" represent the
  // same integer "1".

  // Example 2:
  string ex2_version_a = "1.0";
  string ex2_version_b = "1.0.0";
  int ans2 = 0;
  int res2 = sol.compareVersion(ex2_version_a, ex2_version_b);
  cout << "Test 2" << ": " << res2 << " " << (res2 == ans2 ? "Pass" : "Fail")
       << endl;
  // Explanation: version1 does not specify revision 2, which means it is
  // treated as "0".

  // Example 3:
  string ex3_version_a = "0.1";
  string ex3_version_b = "1.1";
  int ans3 = -1;
  int res3 = sol.compareVersion(ex3_version_a, ex3_version_b);
  cout << "Test 3" << ": " << res3 << " " << (res3 == ans3 ? "Pass" : "Fail")
       << endl;
  // Explanation: version1's revision 0 is "0", while version2's
  // revision 0 is "1". 0 < 1, so version1 < version2.

  // Example 4:
  string ex4_version_a = "1.1";
  string ex4_version_b = "1.10";
  int ans4 = -1;
  int res4 = sol.compareVersion(ex4_version_a, ex4_version_b);
  cout << "Test 4" << ": " << res4 << " " << (res4 == ans4 ? "Pass" : "Fail")
       << endl;

  // Example 5:
  string ex5_version_a = "1.0.1";
  string ex5_version_b = "1";
  int ans5 = 1;
  int res5 = sol.compareVersion(ex5_version_a, ex5_version_b);
  cout << "Test 5" << ": " << res5 << " " << (res5 == ans5 ? "Pass" : "Fail")
       << endl;

  // Constraints:
  // 1 <= version1.length
  // version2.length <= 500
  // version1 and version2 only contain digits and '.'.
  // version1 and version2 are valid version numbers.
  // All the given revisions in version1 and version2 can be
  // stored in a 32-bit integer.
}

int main() {
  Solution1 sol1;
  cout << "Testing Solution1:" << endl;
  test_solution(sol1);
}
