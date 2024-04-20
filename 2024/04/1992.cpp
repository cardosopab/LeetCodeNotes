// 1992. Find All Groups of Farmland
// Medium
// You are given a 0-indexed m x n binary matrix land where a 0 represents a
// hectare of forested land and a 1 represents a hectare of farmland.
//
// To keep the land organized, there are designated rectangular areas of
// hectares that consist entirely of farmland. These rectangular areas are
// called groups. No two groups are adjacent, meaning farmland in one group is
// not four-directionally adjacent to another farmland in a different group.
//
// land can be represented by a coordinate system where the top left corner of
// land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the
// coordinates of the top left and bottom right corner of each group of
// farmland. A group of farmland with a top left corner at (r1, c1) and a bottom
// right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2,
// c2].
//
// Return a 2D array containing the 4-length arrays described above for each
// group of farmland in land. If there are no groups of farmland, return an
// empty array. You may return the answer in any order.

#include <iostream>
#include <ostream>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
  vector<vector<int>> findFarmLand(vector<vector<int>> &land) {
    int R = land.size();
    int C = land[0].size();
    vector<vector<int>> res = {};
    vector<vector<bool>> visited(R, vector<bool>(C, false));

    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (land[r][c] == 1 && !visited[r][c]) {
          int xr = r;
          int xc = c;
          while (xr + 1 < R && land[xr + 1][xc] == 1) {
            xr++;
          }
          while (xc + 1 < C && land[xr][xc + 1] == 1) {
            xc++;
          }
          for (int cr = r; cr <= xr; cr++) {
            for (int cc = c; cc <= xc; cc++) {
              visited[cr][cc] = true;
            }
          }
          res.push_back({r, c, xr, xc});
        }
      }
    }
    return res;
  }
};

void testFindFarmLand() {
  Solution sol;

  // Example 1
  vector<vector<int>> land1 = {{1, 0, 0}, {0, 1, 1}, {0, 1, 1}};
  vector<vector<int>> ans1 = {{0, 0, 0, 0}, {1, 1, 2, 2}};
  vector<vector<int>> result1 = sol.findFarmLand(land1);
  cout << "Example 1: " << (result1 == ans1 ? "Pass" : "Fail") << endl;
  // Explanation:
  // The first group has a top left corner at land[0][0] and a bottom right
  // corner at land[0][0].
  // The second group has a top left corner at land[1][1] and a bottom right
  // corner at land[2][2].

  // Example 2:
  vector<vector<int>> land2 = {{1, 1}, {1, 1}};
  vector<vector<int>> ans2 = {{0, 0, 1, 1}};
  vector<vector<int>> result2 = sol.findFarmLand(land2);
  cout << "Example 2: " << (result2 == ans2 ? "Pass" : "Fail") << endl;
  // Explanation:
  // The first group has a top left corner at land[0][0] and a bottom right
  // corner at land[1][1].

  // Example 3:
  vector<vector<int>> land3 = {{0}};
  vector<vector<int>> ans3 = {};
  vector<vector<int>> result3 = sol.findFarmLand(land3);
  cout << "Example 3: " << (result3 == ans3 ? "Pass" : "Fail") << endl;
  // Explanation:
  // There are no groups of farmland.

  // Example 4:
  vector<vector<int>> land4 = {{0, 1}, {1, 0}};
  vector<vector<int>> ans4 = {{0, 1, 0, 1}, {1, 0, 1, 0}};
  vector<vector<int>> result4 = sol.findFarmLand(land4);
  cout << "Example 4: " << (result4 == ans4 ? "Pass" : "Fail") << endl;

  // Constraints:
  // m == land.length
  // n == land.length
  // 1 <= m, n <= 300
  // land consists of only 0's and 1's.
  // Groups of farmland are rectangular in shape.
}

int main() {
  testFindFarmLand();
  return 0;
}
