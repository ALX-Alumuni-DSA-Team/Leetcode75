Here’s the Leetcode75-style solution for the problem **"Max Number of K-Sum Pairs."**

### Problem Breakdown:
We are given an array `nums` and an integer `k`. We are to find the maximum number of operations where, in each operation, we remove two numbers from the array whose sum equals `k`. The goal is to maximize the number of such operations.

### Approach:
1. **Two-Pointer or Hash Map Approach**:
   - A **hash map** is the best choice here to count the frequency of each number in the array.
   - For each number `num` in the array, we check if there is a complement (`k - num`) already in the hash map.
   - If a complement exists, we can form a pair, so we decrease the frequency of the complement and increase the count of valid operations.
   - If no complement is found, we store the frequency of the current number for future use.

### Python Solution:

```python
from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = Counter(nums)  # Create a frequency map of nums
        operations = 0
        
        for num in nums:
            complement = k - num  # Find the complement needed to form the sum k
            if count[num] > 0 and count[complement] > 0:
                if num == complement and count[num] < 2:
                    continue  # Skip if there's only one occurrence of the number and it equals its complement

                # Decrease counts for both the number and its complement
                count[num] -= 1
                count[complement] -= 1
                operations += 1

        return operations

# Example 1
solution = Solution()
print(solution.maxOperations([1, 2, 3, 4], 5))  # Output: 2

# Example 2
print(solution.maxOperations([3, 1, 3, 4, 3], 6))  # Output: 1
```

### Explanation:

1. **Hash Map (Counter)**:
   - We use a hash map (`Counter(nums)`) to store the frequency of each element in `nums`.

2. **Complement Calculation**:
   - For each element `num` in the array, we calculate the complement `k - num`. We check if there is a complement in the array that hasn't already been used in a pair.

3. **Forming Pairs**:
   - If the complement exists in the hash map and its count is greater than 0, we form a pair by decrementing the count of both `num` and its complement in the hash map.

4. **Edge Case**:
   - If the number is equal to its complement (`num == complement`), we need at least two occurrences of the number to form a valid pair.

5. **Return the Result**:
   - After processing all elements, we return the number of operations (i.e., the number of pairs that sum to `k`).

### Time Complexity:
- **Time Complexity**: O(n), where `n` is the number of elements in the array `nums`. We traverse the array once and perform constant-time operations (using a hash map).
  
- **Space Complexity**: O(n), for storing the frequency map of elements in the array.

### Examples:

#### Example 1:
```plaintext
Input: nums = [1, 2, 3, 4], k = 5
Output: 2
Explanation: 
- First, remove 1 and 4 (sum = 5). 
- Then, remove 2 and 3 (sum = 5). 
There are no more pairs, so the total number of operations is 2.
```

#### Example 2:
```plaintext
Input: nums = [3, 1, 3, 4, 3], k = 6
Output: 1
Explanation:
- First, remove the two 3's (sum = 6). 
- Now nums = [1, 4, 3], and there are no more pairs that sum to 6.
```

### Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

### Key Points:
- We use a hash map to efficiently keep track of the frequency of each element.
- By looking for complements as we traverse the array, we can form pairs in O(n) time.
