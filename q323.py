"""
# Number of Connected Components in an Undirected Graph

You have a graph of `n` nodes.  You are given an integer `n` and an array `edges` where `edges[i] = [aᵢ, bᵢ]` indicates that there is an edge between `aᵢ` and `bᵢ` in the graph.

Return _the number of connected components in the graph_.

**Example 1:**

![Visual representation of the edges in the example](https://i.imgur.com/BCEzWlA.png)
```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```
"""

from typing import List


class Solution:

  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    pass


def run_tests():
  solution = Solution()

  # First we'll do the test case shown in the task description so that will be the one shown to people first if their code isn't working.  If that passes then we'll do other test cases.
  test_cases = [{
    'input': [5, [
      [0, 1],
      [1, 2],
      [3, 4],
    ]],
    'output': 2
  }, {
    'input': [0, []],
    'output': 0
  }, {
    'input': [1, []],
    'output': 1
  }, {
    'input': [2, []],
    'output': 2
  }, {
    'input': [3, []],
    'output': 3
  }, {
    'input': [2, [
      [0, 1],
    ]],
    'output': 1
  }, {
    'input': [3, [
      [0, 1],
    ]],
    'output': 2
  }, {
    'input': [3, [
      [1, 2],
    ]],
    'output': 2
  }, {
    'input': [3, [
      [0, 1],
      [1, 2],
    ]],
    'output': 1
  }]

  for test_case in test_cases:
    input = test_case['input']
    expected_output = test_case['output']
    actual_output = solution.countComponents(*input)
    if not actual_output == expected_output:
      print('Test case failed.\nInput: {}\nExpected: {}\nGot: {}\n'.format(
        input, expected_output, actual_output))
      return
  print("All test cases passed!")
