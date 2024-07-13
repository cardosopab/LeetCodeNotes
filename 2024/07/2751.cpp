// 2751. Robot Collisions
// Hard
// There are n 1-indexed robots, each having a position on a line, health, and
// movement direction.

// You are given 0-indexed integer arrays positions, healths, and a string
// directions (directions[i] is either 'L' for left or 'R' for right). All
// integers in positions are unique.

// All robots start moving on the line simultaneously at the same speed in their
// given directions. If two robots ever share the same position while moving,
// they will collide.

// If two robots collide, the robot with lower health is removed from the line,
// and the health of the other robot decreases by one. The surviving robot
// continues in the same direction it was going. If both robots have the same
// health, they are both removed from the line.

// Your task is to determine the health of the robots that survive the
// collisions, in the same order that the robots were given, i.e. final heath of
// robot 1 (if survived), final health of robot 2 (if survived), and so on. If
// there are no survivors, return an empty array.

// Return an array containing the health of the remaining robots (in the order
// they were given in the input), after no further collisions can occur.

// Note: The positions may be unsorted.

#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

class Solution {
public:
  virtual std::vector<int> survivedRobotsHealths(std::vector<int> &positions,
                                                 std::vector<int> &healths,
                                                 std::string directions) = 0;
};

class Solution1 : public Solution {
public:
  std::vector<int> survivedRobotsHealths(std::vector<int> &positions,
                                         std::vector<int> &healths,
                                         std::string directions) {
    int N = positions.size();
    std::vector<int> indices(N);
    std::vector<int> stack;
    std::iota(indices.begin(), indices.end(), 0);
    std::sort(indices.begin(), indices.end(), [&positions](int a, int b) {
      return positions[a] < positions[b];
    });

    for (int i : indices) {
      // add -> robot to stack
      if (directions[i] == 'R') {
        stack.push_back(i);
        continue;
      }

      // while stack isn't empty and healths[i] > 0
      while (!stack.empty() && healths[i]) {
        int j = stack.back();
        int x = std::min(healths[i], healths[j]);
        // collapse robots
        healths[i] = healths[i] == x ? 0 : healths[i] - 1;
        healths[j] = healths[j] == x ? 0 : healths[j] - 1;
        // pop if healths[j] is 0
        if (!healths[j]) {
          stack.pop_back();
        }
      }
    }

    // return remaining robots
    std::vector<int> ans;
    std::copy_if(healths.begin(), healths.end(), std::back_inserter(ans),
                 [](int h) { return h > 0; });
    return ans;
  };
};

void test_solution(Solution *sol) {
  // Example 1:
  std::vector<int> positions = {5, 4, 3, 2, 1};
  std::vector<int> healths = {2, 17, 9, 15, 10};
  std::string directions = "RRRRR";
  std::vector<int> ans = {2, 17, 9, 15, 10};
  std::vector<int> res =
      sol->survivedRobotsHealths(positions, healths, directions);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: No collision occurs in this example, since all robots are
  // moving in the same direction. So, the health of the robots in order from
  // the first robot is returned, {2, 17, 9, 15, 10}.

  // Example 2:
  positions = {3, 5, 2, 6};
  healths = {10, 10, 15, 12};
  directions = "RLRL";
  ans = {14};
  res = sol->survivedRobotsHealths(positions, healths, directions);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: There are 2 collisions in this example. Firstly, robot 1 and
  // robot 2 will collide, and since both have the same health, they will be
  // removed from the line. Next, robot 3 and robot 4 will collide and since
  // robot 4's health is smaller, it gets removed, and robot 3's health becomes
  // 15 - 1 = 14. Only robot 3 remains, so we return {14}.

  // Example 3:
  positions = {1, 2, 5, 6};
  healths = {10, 10, 11, 11};
  directions = "RLRL";
  ans = {};
  res = sol->survivedRobotsHealths(positions, healths, directions);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';
  // Explanation: Robot 1 and robot 2 will collide and since both have the same
  // health, they are both removed. Robot 3 and 4 will collide and since both
  // have the same health, they are both removed. So, we return an empty array,
  // {}.

  // Example 4:
  positions = {1, 40};
  healths = {10, 11};
  directions = "RL";
  ans = {10};
  res = sol->survivedRobotsHealths(positions, healths, directions);
  std::cout << (res == ans ? "Pass" : "Fail") << '\n';

  // Constraints:
  // 1 <= positions.length == healths.length == directions.length == n <= 105
  // 1 <= positions{i}, healths{i} <= 109
  // directions{i} == 'L' or directions{i} == 'R'
  // All values in positions are distinct
}

int main() {
  Solution1 sol1;
  test_solution(&sol1);
}
