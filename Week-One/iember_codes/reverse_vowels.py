Here’s the Leetcode75-style solution for the problem "Reverse Vowels of a String."

### Problem Breakdown:
We are given a string `s`, and we need to reverse the order of the vowels in the string while keeping the other characters in their original positions. The vowels are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).

### Approach:
1. **Two Pointers**:
   - Use two pointers: one starting from the beginning (`left`) and the other from the end (`right`) of the string.
   - Move the pointers toward each other. When both pointers point to vowels, swap them.
   - Continue this process until the two pointers meet.

2. **Vowel Set**:
   - Create a set of vowels for easy lookup, and handle both lowercase and uppercase vowels.

3. **Result String**:
   - Since strings are immutable in Python, we convert the string to a list, perform the swaps, and then join the list back into a string.

### Python Solution:

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Set of vowels (both lowercase and uppercase)
        s_list = list(s)  # Convert string to a list for easy swapping
        left, right = 0, len(s) - 1  # Initialize two pointers

        while left < right:
            # Move left pointer until we find a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move right pointer until we find a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1

            # Swap the vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return ''.join(s_list)  # Convert list back to string

# Example 1
solution = Solution()
print(solution.reverseVowels("hello"))  # Output: "holle"

# Example 2
print(solution.reverseVowels("leetcode"))  # Output: "leotcede"
```

### Explanation:

1. **Initialize Pointers**:
   - We initialize two pointers: `left` at the start of the string and `right` at the end.
   
2. **Skip Non-Vowels**:
   - Move the `left` pointer forward until it finds a vowel.
   - Move the `right` pointer backward until it finds a vowel.

3. **Swap Vowels**:
   - Once both pointers are pointing to vowels, swap them.
   - Move both pointers inward and repeat the process until they meet or cross.

4. **Return the Result**:
   - Convert the list back to a string using `''.join(s_list)` and return the result.

### Time Complexity:
- **Time Complexity**: O(n), where `n` is the length of the string. Each character is processed at most once as the two pointers traverse the string.
  
- **Space Complexity**: O(n), due to the list used to hold the characters of the string.

### Examples:

#### Example 1:
Input: s = "hello"
Output: "holle"
Explanation: The vowels 'e' and 'o' are reversed.
```

#### Example 2:
Input: s = "leetcode"
Output: "leotcede"
Explanation: The vowels 'e', 'e', and 'o' are reversed.
```

### Constraints:
- The length of the string is guaranteed to be between 1 and \(3 \times 10^5\), and the string consists of printable ASCII characters, so the solution should handle large inputs efficiently.

This approach is optimal and uses the two-pointer technique to reverse the vowels while leaving the non-vowel characters in their original positions.
