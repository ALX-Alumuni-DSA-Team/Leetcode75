Here’s the Leetcode75-style solution for the problem "Is Subsequence."

### Problem Breakdown:
We are given two strings `s` and `t`. We need to determine if `s` is a subsequence of `t`. A subsequence means that all characters in `s` appear in `t` in the same order, but they don’t need to be contiguous.

### Approach:
1. **Two-Pointer Approach**:
   - Use two pointers: one (`i`) to traverse the string `s` and another (`j`) to traverse the string `t`.
   - As we move through `t`, if the character at `t[j]` matches the character at `s[i]`, we increment the pointer `i` (indicating we found a matching character in `t` for the current character in `s`).
   - If we can successfully match all characters in `s` before the end of `t`, then `s` is a subsequence of `t`.

2. **Result**:
   - If `i` reaches the length of `s`, return `True` (indicating all characters in `s` were found in order within `t`). Otherwise, return `False`.

### Python Solution:

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        # Loop through both strings
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move pointer for s
                i += 1
            j += 1  # Always move pointer for t
        
        # If i reached the end of s, it means all characters of s were found in t in order
        return i == len(s)

# Example 1
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: True

# Example 2
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: False
```

### Explanation:

1. **Two-Pointer Technique**:
   - We use two pointers, `i` for `s` and `j` for `t`. We traverse `t` using `j`, and each time we find a matching character with `s[i]`, we increment `i`. We always increment `j` to continue moving through `t`.
   
2. **Early Termination**:
   - The loop exits either when `i` reaches the end of `s` (which means `s` is a subsequence of `t`), or when `j` reaches the end of `t`.

3. **Return Condition**:
   - If we successfully traverse all of `s` (i.e., `i == len(s)`), return `True`, otherwise return `False`.

### Time Complexity:
- **Time Complexity**: O(n), where `n` is the length of `t`. We make a single pass through `t`, comparing characters from `s`.
  
- **Space Complexity**: O(1), since no extra space is used except for the two pointers.

### Examples:

#### Example 1:
```plaintext
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: "abc" appears in "ahbgdc" in the correct order: 'a', 'b', 'c'.
```

#### Example 2:
```plaintext
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: "axc" does not appear in "ahbgdc" because 'x' is missing.
```

### Constraints:
- The length of `s` is between 0 and 100, and the length of `t` is between 0 and \(10^4\).
- Both `s` and `t` consist only of lowercase English letters.

This approach efficiently checks if `s` is a subsequence of `t` by traversing both strings with two pointers, ensuring that the characters appear in the correct order.
