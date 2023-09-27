"""
# Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode`

**Example 1:**

```
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Explanation:
One possible encode method is: "lint:;code:;love:;you"
```

**Example 2:**

```
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]

Explanation:
One possible encode method is: "we:;say:;:::;yes"
```
"""


from typing import List


class Solution:

  def encode(self, list_of_strings: List[str]) -> str:
    pass

  def decode(self, encoded_strings: str) -> List[str]:
    pass


def run_tests():
  solution = Solution()

  # First we'll do the test case shown in the task description so that will be the one shown to people first if their code isn't working.  If that passes then we'll do other test cases.
  test_cases = [{
    'input': ["lint", "code", "love", "you"],
    'output': ["lint", "code", "love", "you"]
  }, {
    'input': ["we", "say", ":", "yes"]
  }]

  for test_case in test_cases:
    input = test_case['input']

    encoded_string = solution.encode(input)
    if not isinstance(encoded_string, str):
      print(
        'Test case failed.\nInput: {}\nExpected encode() return type to be str\nGot: {}\n'
        .format(input, type(encoded_string)))
      return

    decoded_string = solution.decode(encoded_string)
    if not decoded_string == input:
      print('Test case decode() failed.\nExpected: {}\nGot: {}\n'.format(
        input, decoded_string))
      return
  print("All test cases passed!")
