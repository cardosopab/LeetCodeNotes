// 1442. Count Triplets That Can Form Two Arrays of Equal XOR
// Medium
// Given an array of integers arr.
//
// We want to select three indices i, j and k where (0 <= i < j <= k <
// arr.length).
//
// Let's define a and b as follows:
//
// a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
// b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
// Note that ^ denotes the bitwise-xor operation.
//
// Return the number of triplets (i, j and k) Where a == b.

#include <iostream>
#include <vector>

class Solution {
public:
  virtual int countTriplets(std::vector<int> &arr) = 0;
};

class Solution1 : public Solution {
public:
  int countTriplets(std::vector<int> &arr) {
    int res = 0;
    int N = arr.size();

    for (int i = 0; i < N; i++) {
      int a = 0;
      for (int j = i; j < N; j++) {
        a ^= arr[j];
        int b = 0;
        for (int k = j + 1; k < N; k++) {
          b ^= arr[k];
          if (a == b) {
            res++;
          }
        }
      }
    }
    return res;
  };
};

void test_solution(Solution &sol) {
  // Example 1:
  std::vector<int> arr1 = {2, 3, 1, 6, 7};
  int ans1 = 4;
  int res1 = sol.countTriplets(arr1);
  std::cout << (ans1 == res1 ? "Pass" : "Fail") << std::endl;
  // Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
  //
  // Example 2:
  std::vector<int> arr2 = {1, 1, 1, 1, 1};
  int ans2 = 10;
  int res2 = sol.countTriplets(arr2);
  std::cout << (ans2 == res2 ? "Pass" : "Fail") << std::endl;
  //
  // Constraints:
  // 1 <= arr.length <= 300
  // 1 <= arr[i] <= 108
}

int main() {
  Solution1 sol1;
  test_solution(sol1);
}
