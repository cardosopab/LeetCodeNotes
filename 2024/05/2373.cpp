// 2373. Largest Local Values in a Matrix
// Easy
// You are given an n x n integer matrix grid.
//
// Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
//
// maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid
// centered around row i + 1 and column j + 1. In other words, we want to find
// the largest value in every contiguous 3 x 3 matrix in grid.
//
// Return the generated matrix.
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  virtual vector<vector<int>> largestLocal(vector<vector<int>> &grid) = 0;
};

class Solution1 : public Solution {
public:
  vector<vector<int>> largestLocal(vector<vector<int>> &grid) {
    int N = grid.size();
    int minus_2 = N - 2;
    vector<vector<int>> ans(minus_2, vector<int>(minus_2, 0));

    for (int r = 0; r < minus_2; r++) {
      for (int c = 0; c < minus_2; c++) {
        for (int i = 0; i < 3; i++) {
          for (int j = 0; j < 3; j++) {
            ans[r][c] = max(ans[r][c], grid[r + i][c + j]);
          }
        }
      }
    }
    return ans;
  }
};

void test_solution(Solution &sol) {
  // Example 1:
  vector<vector<int>> grid1 = {
      {9, 9, 8, 1}, {5, 6, 2, 6}, {8, 2, 6, 4}, {6, 2, 2, 2}};
  vector<vector<int>> ans1{{9, 9}, {8, 6}};
  vector<vector<int>> res1 = sol.largestLocal(grid1);
  cout << (res1 == ans1 ? "Pass" : "Fail") << endl;
  // Explanation: The diagram above shows the original matrix and the generated
  // matrix. Notice that each value in the generated matrix corresponds to the
  // largest value of a contiguous 3 x 3 matrix in grid. Example 2:
  //
  // Example 2:
  vector<vector<int>> grid2 = {{1, 1, 1, 1, 1},
                               {1, 1, 1, 1, 1},
                               {1, 1, 2, 1, 1},
                               {1, 1, 1, 1, 1},
                               {1, 1, 1, 1, 1}};
  vector<vector<int>> ans2{{2, 2, 2}, {2, 2, 2}, {2, 2, 2}};
  vector<vector<int>> res2 = sol.largestLocal(grid2);
  cout << (res2 == ans2 ? "Pass" : "Fail") << endl;
  // Explanation: Notice that the 2 is contained within every contiguous 3 x 3
  // matrix in grid.
  //
  //
  // Constraints:
  // n == grid.length == grid{i}.length
  // 3 <= n <= 100
  // 1 <= grid{i}{j} <= 100
}

int main() {
  Solution1 sol1;
  test_solution(sol1);
  return 0;
}
