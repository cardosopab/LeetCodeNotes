//  463. Island Perimeter
//  Easy
//  You are given row x col grid representing a map where grid[i][j] = 1
//  represents land and grid[i][j] = 0 represents water. Grid cells are
//  connected horizontally/vertically (not diagonally). The grid is completely
//  surrounded by water, and there is exactly one island (i.e., one or more
//  connected land cells). The island doesn't have "lakes", meaning the water
//  inside isn't connected to the water around the island. One cell is a square
//  with side length 1. The grid is rectangular, width and height don't exceed
//  100. Determine the perimeter of the island.


#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
  int islandPerimeter(vector<vector<int>> &grid) {
    const int R = grid.size();
    const int C = grid[0].size();
    const vector<vector<int>> directions = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1},
    };
    int ans = 0;

    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (grid[r][c] == 1) {
          for (int i = 0; i < directions.size(); i++) {
            int dr = directions[i][0];
            int dc = directions[i][1];
            int xr = r + dr;
            int xc = c + dc;
            bool is_greater = xr >= 0 && xc >= 0;
            bool is_less = xr < R && xc < C;

            if (is_greater && is_less) {
              if (grid[xr][xc] == 0) {
                ans++;
              }
            } else if (is_greater) {
              ans++;
            } else if (is_less) {
              ans++;
            }
          }
        }
      }
    }
    return ans;
  }
};


void testIslandPerimeter() {
    Solution sol;

    // Example 1
    vector<vector<int>> grid1 = {
        {0, 1, 0, 0},
        {1, 1, 1, 0},
        {0, 1, 0, 0},
        {1, 1, 0, 0}
    };
    int ans1 = 16;
    int result1 = sol.islandPerimeter(grid1);
    cout << "Example 1: " << (result1 == ans1 ? "Pass" : "Fail") << endl;

    // Example 2
    vector<vector<int>> grid2 = {{1}};
    int ans2 = 4;
    int result2 = sol.islandPerimeter(grid2);
    cout << "Example 2: " << (result2 == ans2 ? "Pass" : "Fail") << endl;

    // Example 3
    vector<vector<int>> grid3 = {{1, 0}};
    int ans3 = 4;
    int result3 = sol.islandPerimeter(grid3);
    cout << "Example 3: " << (result3 == ans3 ? "Pass" : "Fail") << endl;
}

int main() {
    testIslandPerimeter();
    return 0;
}