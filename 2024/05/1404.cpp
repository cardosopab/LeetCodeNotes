// 1404. Number of Steps to Reduce a Number in Binary Representation to One
// Medium
// Given the binary representation of an integer as a string s, return the
// number of steps to reduce it to 1 under the following rules:
//
// If the current number is even, you have to divide it by 2.
//
// If the current number is odd, you have to add 1 to it.
//
// It is guaranteed that you can always reach one for all test cases.

#include <iostream>
#include <string>
class Solution {
public:
  virtual int numSteps(std::string s) = 0;
};
class Solution1 : public Solution {
public:
  int numSteps(std::string s) {
    int res = 0;
    int carry = 0;

    for (int i = s.size() - 1; i > 0; i--) {
      int curr = (int(s[i]) + carry) % 2;

      switch (curr) {
      case 0:
        res++;
        break;
      case 1:
        res += 2;
        carry = 1;
        break;
      }
    };
    res = res + carry;
    return res;
  }
};

// NOTE: Second solution does not pass because of number overflow.
class Solution2 : public Solution {
public:
  int numSteps(std::string s) {
    long long n = std::stoull(s, nullptr, 2);
    // std::cout << n << std::endl;
    int ans = 0;

    if (n < 0) {
      n = -n;
    }

    while (n > 1) {
      ans++;
      if (n % 2 == 0) {
        n /= 2;
      } else {
        n++;
      }
    }
    return ans;
  };
};

void test_solution(Solution &sol) {
  // Example 1:
  std::string s1 = "1101";
  int ans1 = 6;
  int res1 = sol.numSteps(s1);
  std::cout << (ans1 == res1 ? "Pass" : "Fail") << std::endl;
  // Explanation: "1101" corressponds to number 13 in their decimal
  // representation. Step 1) 13 is odd, add 1 and obtain 14. Step 2) 14 is
  // even, divide by 2 and obtain 7. Step 3) 7 is odd, add 1 and obtain 8.
  // Step 4) 8 is even, divide by 2 and obtain 4. Step 5) 4 is even, divide by
  // 2 and obtain 2. Step 6) 2 is even, divide by 2 and obtain 1.

  // Example 2:
  std::string s2 = "10";
  int ans2 = 1;
  int res2 = sol.numSteps(s2);
  std::cout << (ans2 == res2 ? "Pass" : "Fail") << std::endl;
  // Explanation: "10" corressponds to number 2 in their decimal
  // representation. Step 1) 2 is even, divide by 2 and obtain 1.

  // Example 3:
  std::string s3 = "1";
  int ans3 = 0;
  int res3 = sol.numSteps(s3);
  std::cout << (ans3 == res3 ? "Pass" : "Fail") << std::endl;

  // Example 4:
  std::string s4 =
      "1111110011101010110011100100101110010100101110111010111110110010";
  int ans4 = 89;
  int res4 = sol.numSteps(s4);
  std::cout << (ans4 == res4 ? "Pass" : "Fail") << std::endl;

  //
  // Constraints:
  // 1 <= s.length <= 500
  // s consists of characters '0' or '1'
  // s[0] == '1'
}

int main() {
  std::cout << "Test 1:" << std::endl;
  Solution1 sol1;
  test_solution(sol1);
  std::cout << "Test 2:" << std::endl;
  Solution2 sol2;
  test_solution(sol2);
  return 0;
}
