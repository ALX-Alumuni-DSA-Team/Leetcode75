To solve the **Increasing Triplet Subsequence** problem, we need to determine if there exists three indices \(i\), \(j\), and \(k\) in the array `nums` such that:

- \(i < j < k\)
- \(nums[i] < nums[j] < nums[k]\)

The challenge requires a solution that runs in \(O(n)\) time complexity and \(O(1)\) space complexity.

### Solution Strategy:

We can solve this problem using a greedy approach with two variables:
- **`first`**: This keeps track of the smallest number encountered so far.
- **`second`**: This keeps track of the second smallest number that is greater than `first`.

The algorithm proceeds as follows:
1. Iterate through the array `nums`.
2. If the current number is smaller than `first`, update `first`.
3. If the current number is larger than `first` but smaller than `second`, update `second`.
4. If the current number is larger than both `first` and `second`, we have found an increasing triplet subsequence, and we return `true`.
5. If no such triplet is found, return `false`.

### LeetCode75 Solution in Python:

Here’s the Python implementation:

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables to represent the smallest and second smallest elements
        first = float('inf')
        second = float('inf')
        
        # Traverse through the array
        for num in nums:
            if num <= first:
                # Update first if the current number is smaller or equal to first
                first = num
            elif num <= second:
                # Update second if the current number is larger than first but smaller than or equal to second
                second = num
            else:
                # If we find a number larger than both first and second, return True
                return True
        
        # If no increasing triplet subsequence is found, return False
        return False

# Example usage:
# solution = Solution()
# print(solution.increasingTriplet([1, 2, 3, 4, 5]))   # Output: True
# print(solution.increasingTriplet([5, 4, 3, 2, 1]))   # Output: False
# print(solution.increasingTriplet([2, 1, 5, 0, 4, 6])) # Output: True
```

### Explanation of the Code:

1. **Initialize `first` and `second`**:
   - `first` and `second` are initialized to positive infinity (`float('inf')`) to represent the smallest and second smallest numbers found so far.

2. **Iterate through the array**:
   - For each element `num` in the array `nums`, check:
     - If `num` is smaller than or equal to `first`, update `first`.
     - If `num` is larger than `first` but smaller than or equal to `second`, update `second`.
     - If `num` is larger than both `first` and `second`, return `true` because an increasing triplet has been found.

3. **Return `false` if no triplet is found**:
   - If the loop completes without finding an increasing triplet, return `false`.

### Example Walkthrough:

#### Example 1:
- Input: `nums = [1, 2, 3, 4, 5]`
  - `first = 1`, `second = 2`, and we encounter `3`, which is greater than both `1` and `2`.
  - Return `true`.

#### Example 2:
- Input: `nums = [5, 4, 3, 2, 1]`
  - We continuously update `first` and `second` to the current number, but no triplet is found where \(nums[i] < nums[j] < nums[k]\).
  - Return `false`.

#### Example 3:
- Input: `nums = [2, 1, 5, 0, 4, 6]`
  - `first = 1`, `second = 4`, and we encounter `6`, which is greater than both `1` and `4`.
  - Return `true`.

### Constraints Handling:

- **Time Complexity**: The solution runs in \(O(n)\), where \(n\) is the length of the input array `nums`, because we only iterate through the array once.
- **Space Complexity**: The space complexity is \(O(1)\), since we use only two extra variables `first` and `second`.

This solution efficiently solves the problem by keeping track of the smallest and second smallest numbers encountered, adhering to the required time and space complexity.
