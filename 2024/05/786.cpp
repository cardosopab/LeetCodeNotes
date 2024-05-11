// 786. K-th Smallest Prime Fraction
// Medium
// You are given a sorted integer array arr containing 1 and prime numbers,
// where all the integers of arr are unique. You are also given an integer k.
//
// For every i and j where 0 <= i < j < arr.length, we consider the fraction
// arr[i] / arr[j].
//
// Return the kth smallest fraction considered. Return your answer as an array
// of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
//
//
//
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
  virtual vector<int> kthSmallestPrimeFraction(vector<int> &arr, int k) = 0;
};

class Solution1 : public Solution {
public:
  vector<int> kthSmallestPrimeFraction(vector<int> &arr, int k) {
    int N = arr.size();
    vector<pair<double, pair<int, int>>> vec;

    for (int i = 0; i < N; i++) {
      for (int j = i + 1; j < N; j++) {
        double fraction = static_cast<double>(arr[i] / (arr[j] / 1.0));
        vec.push_back({fraction, {arr[i], arr[j]}});
      }
    }
    sort(vec.begin(), vec.end());
    return {vec[k - 1].second.first, vec[k - 1].second.second};
  }
};

class Solution2 : public Solution {
public:
  vector<int> kthSmallestPrimeFraction(vector<int> &arr, int k) {
    int n = arr.size();
    priority_queue<pair<double, pair<int, int>>,
                   vector<pair<double, pair<int, int>>>,
                   greater<pair<double, pair<int, int>>>>
        pq;
    for (int i = 0; i < n - 1; i++)
      pq.push({arr[i] / (arr[n - 1] / 1.0), {i, n - 1}});
    for (int i = 0; i < k - 1; i++) {
      int a = pq.top().second.first;
      int b = pq.top().second.second - 1;
      pq.pop();
      if (b > a)
        pq.push({arr[a] / (arr[b] / 1.0), {a, b}});
    }
    return {arr[pq.top().second.first], arr[pq.top().second.second]};
  }
};

void test_solution(Solution &sol) {

  // Example 1:
  vector<int> arr1 = {1, 2, 3, 5};
  int k1 = 3;
  vector<int> ans1 = {2, 5};
  vector<int> res1 = sol.kthSmallestPrimeFraction(arr1, k1);
  cout << "Test 1 : " << res1[0] << "," << res1[1] << " "
       << (res1 == ans1 ? "Pass" : "Fail") << endl;
  // Explanation: The fractions to be considered in sorted order are:
  // 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
  // The third fraction is 2/5.
  //
  // Example 2:
  vector<int> arr2 = {1, 7};
  int k2 = 1;
  vector<int> ans2 = {1, 7};
  vector<int> res2 = sol.kthSmallestPrimeFraction(arr2, k2);
  cout << "Test 2 : " << res2[0] << "," << res2[1] << " "
       << (res2 == ans2 ? "Pass" : "Fail") << endl;

  // Constraints:
  // 2 <= .length <= 1000
  // 1 <= [i] <= 3 * 104
  // [0] == 1
  // [i] is a prime number for i > 0.
  // All the numbers of  are unique and sorted in strictly increasing order.
  // 1 <= k <= .length * (arr.length - 1) / 2
  //
}
int main() {
  Solution1 sol1;
  test_solution(sol1);
  Solution2 sol2;
  test_solution(sol2);
  return 0;
}
