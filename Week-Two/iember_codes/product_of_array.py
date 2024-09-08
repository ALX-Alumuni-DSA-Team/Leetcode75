To solve the problem of finding the product of the array except for the element at each index, we need to calculate the result for each index without using division and ensure the solution runs in \(O(n)\) time complexity.

### Steps to Solve the Problem

1. **Left Products**: For each element at index `i`, compute the product of all the elements to the left of `i`.
   
2. **Right Products**: For each element at index `i`, compute the product of all the elements to the right of `i`.

3. **Combine Left and Right Products**: For each index `i`, the product of the array except for the element at `i` is the product of the left and right products.

### Solution Strategy

- We use two passes:
  - **First Pass**: Calculate the left products for each element.
  - **Second Pass**: Calculate the right products and multiply them with the left products to get the result.

### LeetCode75 Solution in Python

Here’s the Python implementation:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Calculate left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Step 2: Calculate right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

# Example usage:
# solution = Solution()
# print(solution.productExceptSelf([1, 2, 3, 4]))    # Output: [24, 12, 8, 6]
# print(solution.productExceptSelf([-1, 1, 0, -3, 3])) # Output: [0, 0, 9, 0, 0]
```

### Explanation of the Code

1. **Initialize the Result Array**: 
   - We initialize an array `answer` of length `n` where each element is `1`. This array will store the final results.

2. **Calculate Left Products**:
   - We iterate from left to right and calculate the product of all elements to the left of each index.
   - `left_product` is initialized to `1`, and for each element `i`, `answer[i]` is updated with the current `left_product`. Then, `left_product` is updated by multiplying it with `nums[i]`.

3. **Calculate Right Products**:
   - We iterate from right to left and calculate the product of all elements to the right of each index.
   - `right_product` is initialized to `1`, and for each element `i`, we multiply `answer[i]` by the current `right_product`. Then, `right_product` is updated by multiplying it with `nums[i]`.

### Example Walkthrough

#### Example 1:
- Input: `nums = [1, 2, 3, 4]`
  
  **Left Pass**:
  - Initialize `left_product = 1` and `answer = [1, 1, 1, 1]`.
  - At index 0, `answer[0] = 1`, update `left_product = 1 * nums[0] = 1`.
  - At index 1, `answer[1] = 1`, update `left_product = 1 * nums[1] = 2`.
  - At index 2, `answer[2] = 2`, update `left_product = 2 * nums[2] = 6`.
  - At index 3, `answer[3] = 6`, update `left_product = 6 * nums[3] = 24`.

  **Right Pass**:
  - Initialize `right_product = 1`.
  - At index 3, `answer[3] *= 1`, update `right_product = 1 * nums[3] = 4`.
  - At index 2, `answer[2] *= 4`, update `right_product = 4 * nums[2] = 12`.
  - At index 1, `answer[1] *= 12`, update `right_product = 12 * nums[1] = 24`.
  - At index 0, `answer[0] *= 24`.

- Output: `[24, 12, 8, 6]`

#### Example 2:
- Input: `nums = [-1, 1, 0, -3, 3]`
  
  **Left Pass**:
  - Initialize `left_product = 1` and `answer = [1, 1, 1, 1, 1]`.
  - At index 0, `answer[0] = 1`, update `left_product = -1`.
  - At index 1, `answer[1] = -1`, update `left_product = -1`.
  - At index 2, `answer[2] = -1`, update `left_product = 0`.
  - At index 3, `answer[3] = 0`, update `left_product = 0`.
  - At index 4, `answer[4] = 0`, update `left_product = 0`.

  **Right Pass**:
  - Initialize `right_product = 1`.
  - At index 4, `answer[4] *= 1`, update `right_product = 3`.
  - At index 3, `answer[3] *= 3`, update `right_product = -9`.
  - At index 2, `answer[2] *= -9`, update `right_product = 0`.
  - At index 1, `answer[1] *= 0`, update `right_product = 0`.
  - At index 0, `answer[0] *= 0`.

- Output: `[0, 0, 9, 0, 0]`

### Constraints Handling

- **Time Complexity**: The solution runs in \(O(n)\), where \(n\) is the length of the input array `nums`. We traverse the array twice (once for left products and once for right products), so the total time complexity is linear.

- **Space Complexity**: The space complexity is \(O(1)\) for the extra space used (since we are using the result array `answer` as output, which doesn't count as extra space).

This solution adheres to the problem's constraints, making it both time-efficient and space-efficient.
