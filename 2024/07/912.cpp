// 912. Sort an Array
// Medium
// Given an array of integers nums, sort the array in ascending order and return
// it.

// You must solve the problem without using any built-in functions in O(nlog(n))
// time complexity and with the smallest space complexity possible.

#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>
#include <vector>

class Solution
{
public:
  virtual std::vector<int> sortArray(std::vector<int> &nums) = 0;
};

class Solution1 : public Solution
{
public:
  std::vector<int> sortArray(std::vector<int> &nums)
  {
    std::deque<int> q;
    std::vector<int> ans;
    std::move(nums.begin(), nums.end(), std::back_inserter(q));
    q = merge_sort(q);
    std::move(q.begin(), q.end(), std::back_inserter(ans));
    return ans;
  }

  std::deque<int> merge_sort(std::deque<int> q)
  {
    if (q.size() < 2)
    {
      return q;
    }

    std::deque<int> ans;
    int mid = q.size() / 2;
    auto left = merge_sort(std::deque<int>(q.begin(), q.begin() + mid));
    auto right = merge_sort(std::deque<int>(q.begin() + mid, q.end()));

    while (!left.empty() && !right.empty())
    {
      if (left.front() < right.front())
      {
        ans.push_back(left.front());
        left.pop_front();
      }
      else
      {
        ans.push_back(right.front());
        right.pop_front();
      }
    }
    std::copy(left.begin(), left.end(), std::back_inserter(ans));
    std::copy(right.begin(), right.end(), std::back_inserter(ans));
    return ans;
  }
};

class Solution2 : public Solution
{
public:
  std::vector<int> sortArray(std::vector<int> &nums)
  {
    merge_sort(nums, 0, nums.size() - 1);
    return nums;
  }

  void merge_sort(std::vector<int> &nums, int left, int right)
  {
    if (left >= right)
    {
      return;
    }

    int mid = left + (right - left) / 2;

    merge_sort(nums, left, mid);
    merge_sort(nums, mid + 1, right);
    merge(nums, left, mid, right);
  }

  void merge(std::vector<int> &nums, int left, int mid, int right)
  {
    int left_size = mid - left + 1;
    int right_size = right - mid;

    std::vector<int> left_vec(left_size);
    std::vector<int> right_vec(right_size);

    for (int i = 0; i < left_size; i++)
    {
      left_vec[i] = nums[left + i];
    }
    for (int i = 0; i < right_size; i++)
    {
      right_vec[i] = nums[mid + 1 + i];
    }

    int i = 0, j = 0, k = left;
    while (i < left_size && j < right_size)
    {
      if (left_vec[i] < right_vec[j])
      {
        nums[k++] = left_vec[i++];
      }
      else
      {
        nums[k++] = right_vec[j++];
      }
    }

    while (i < left_size)
    {
      nums[k++] = left_vec[i++];
    }
    while (j < right_size)
    {
      nums[k++] = right_vec[j++];
    }
  }
};

void test_solution(Solution *sol)
{
  // Example 1:
  std::vector<int> nums = {5, 2, 3, 1};
  std::vector<int> ans = {1, 2, 3, 5};
  std::vector<int> res = sol->sortArray(nums);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';

  // Explanation: After sorting the array, the positions of some numbers are not
  // changed (for example, 2 and 3), while the positions of other numbers are
  // changed (for example, 1 and 5).

  // Example 2:
  nums = {5, 1, 1, 2, 0, 0};
  ans = {0, 0, 1, 1, 2, 5};
  res = sol->sortArray(nums);
  std::cout << (ans == res ? "Pass" : "Fail") << '\n';
  // Explanation: Note that the values of nums are not necessairly unique.

  // Constraints:
  // 1 <= nums.length <= 5 * 104
  // -5 * 104 <= nums{i} <= 5 * 104
}

int main()
{
  std::cout << "Test 1" << '\n';
  Solution1 sol1;
  test_solution(&sol1);
  std::cout << "Test 2" << '\n';
  Solution2 sol2;
  test_solution(&sol2);
}
