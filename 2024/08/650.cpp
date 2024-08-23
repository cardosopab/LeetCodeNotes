#include <algorithm>
#include <climits>
#include <iostream>

class Solution {
public:
  int minSteps(int N) {
    if (N == 1) {
      return 0;
    }
    return 1 + get_min(1, 1, N);
  }

  int get_min(int curr, int clip, int N) {
    int INF = 1000;
    if (curr > N) {
      return INF;
    }
    if (curr == N) {
      return 0;
    }

    int best = INF;
    // paste
    best = std::min(best, get_min(curr + clip, clip, N) + 1);

    // copy & paste
    best = std::min(best, get_min(curr + curr, curr, N) + 2);

    return best;
  }
};

int main() {
  int n = 3;
  int ans = 3;
  int res = Solution().minSteps(n);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  n = 1;
  ans = 0;
  res = Solution().minSteps(n);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
}
