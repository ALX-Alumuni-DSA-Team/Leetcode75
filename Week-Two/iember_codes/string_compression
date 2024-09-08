To solve the **String Compression** problem, the goal is to modify the input array `chars` in-place so that consecutive repeating characters are compressed into the format: `character + count`. The final compressed string should replace the original characters in the array and return the new length of the array.

### Solution Approach:

1. **Two-pointer technique**:
   - Use one pointer (`write`) to modify the input array in place and another pointer (`read`) to iterate over the input array.
   - Count consecutive repeating characters as you iterate through the array.

2. **Compression rule**:
   - If a character appears more than once consecutively, write the character followed by the count.
   - If a character appears only once, write the character without a count.

3. **Group lengths**:
   - When a character appears more than once, its count may be greater than 9, so we need to split the count digits (e.g., 12 becomes "1" and "2") and write them separately in the array.

4. **Return value**:
   - Return the length of the modified array.

### LeetCode75 Solution in Python:

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer to write the compressed characters
        read = 0   # Pointer to read through the original array
        
        while read < len(chars):
            current_char = chars[read]
            count = 0
            
            # Count consecutive occurrences of the current character
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1
            
            # Write the current character
            chars[write] = current_char
            write += 1
            
            # If count > 1, write the count as individual digits
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
```

### Explanation of the Code:

1. **Initialize Pointers**:
   - `write`: This pointer keeps track of where to write the compressed characters in the array.
   - `read`: This pointer iterates through the array to count consecutive characters.

2. **Iterate through the array**:
   - For each unique character (i.e., `current_char`), count its consecutive occurrences.
   - Move the `read` pointer to count how many times the current character repeats.

3. **Write the compressed result**:
   - Write the current character to the `write` pointer.
   - If the count of consecutive occurrences is greater than 1, convert the count to a string and write each digit of the count separately.

4. **Return the new length**:
   - After compressing the array, the `write` pointer will point to the new length of the compressed array, which is returned.

### Example Walkthrough:

#### Example 1:
- Input: `chars = ["a", "a", "b", "b", "c", "c", "c"]`
  
  **Step-by-Step Compression**:
  - `current_char = 'a'`, count = 2 → Write `['a', '2']`.
  - `current_char = 'b'`, count = 2 → Write `['b', '2']`.
  - `current_char = 'c'`, count = 3 → Write `['c', '3']`.

  **Result**:
  - The first 6 characters of the input array become: `["a", "2", "b", "2", "c", "3"]`.
  - Output: `6`.

#### Example 2:
- Input: `chars = ["a"]`
  
  **Step-by-Step Compression**:
  - `current_char = 'a'`, count = 1 → Write `['a']`.

  **Result**:
  - The array remains unchanged as `["a"]`.
  - Output: `1`.

#### Example 3:
- Input: `chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]`
  
  **Step-by-Step Compression**:
  - `current_char = 'a'`, count = 1 → Write `['a']`.
  - `current_char = 'b'`, count = 12 → Write `['b', '1', '2']`.

  **Result**:
  - The first 4 characters of the input array become: `["a", "b", "1", "2"]`.
  - Output: `4`.

### Time and Space Complexity:

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the `chars` array. We iterate through the array once, and writing to the array takes constant time for each character or digit.
  
- **Space Complexity**: \(O(1)\), because the solution modifies the input array in place and uses only constant extra space.

This solution is efficient, meeting the problem’s constraints of constant space and linear time complexity.
