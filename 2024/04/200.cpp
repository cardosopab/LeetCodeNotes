// 200. Number of Islands
// Medium
// Given an m x n 2D binary grid grid which represents a map of '1's (land) and
// '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands
// horizontally or vertically. You may assume all four edges of the grid are all
// surrounded by water.

#include <iostream>
#include <ostream>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
  int numIslands(vector<vector<char>> &grid) {
    const int R = grid.size();
    const int C = grid[0].size();
    vector<vector<bool>> visited(R, vector<bool>(C, false));

    int islands = 0;
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (grid[r][c] == '1' && !visited[r][c]) {
          islands += 1;
          dfs(r, c, visited, grid);
        }
      }
    }
    return islands;
  }

public:
  void dfs(int r, int c, vector<vector<bool>> &visited,
           vector<vector<char>> &grid) {
    const int R = grid.size();
    const int C = grid[0].size();
    const vector<pair<int, int>> directions = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1},
    };

    visited[r][c] = true;

    for (auto d : directions) {
      int xr = r + d.first;
      int xc = c + d.second;
      bool is_greater = xc >= 0 && xr >= 0;
      bool is_less = xr < R && xc < C;
      if (is_greater && is_less && !visited[xr][xc] && grid[xr][xc] == '1') {
        dfs(xr, xc, visited, grid);
      }
    }
  }
};

void testNumIslands() {
  Solution sol;

  // Example 1
  vector<vector<char>> grid1 = {
      {'1', '1', '1', '1', '0'},
      {'1', '1', '0', '1', '0'},
      {'1', '1', '0', '0', '0'},
      {'0', '0', '0', '0', '0'},
  };
  int ans1 = 1;
  int result1 = sol.numIslands(grid1);
  cout << "Example 1: " << (result1 == ans1 ? "Pass" : "Fail") << endl;

  // Example 2
  vector<vector<char>> grid2 = {
      {'1', '1', '0', '0', '0'},
      {'1', '1', '0', '0', '0'},
      {'0', '0', '1', '0', '0'},
      {'0', '0', '0', '1', '1'},
  };
  int ans2 = 3;
  int result2 = sol.numIslands(grid2);
  cout << "Example 2: " << (result2 == ans2 ? "Pass" : "Fail") << endl;
}
// Constraints:

// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 300
// grid[i][j] is '0' or '1'.

int main() {
  testNumIslands();
  return 0;
}