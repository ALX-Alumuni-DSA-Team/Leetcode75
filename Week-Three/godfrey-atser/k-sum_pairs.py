class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Dictionary to store the frequency of each number
        num_count = {}
        operations = 0
        
        # Iterate through the numbers in the array
        for num in nums:
            complement = k - num
            
            # Check if the complement exists in the hash map
            if num_count.get(complement, 0) > 0:
                # Perform an operation (remove the pair)
                operations += 1
                # Decrease the complement count
                num_count[complement] -= 1
            else:
                # Add the current number to the hash map
                num_count[num] = num_count.get(num, 0) + 1
        
        return operations

# Instantiate the Solution class
solution = Solution()

# Example usage
# Example 1
nums1 = [1, 2, 3, 4]
k1 = 5
result1 = solution.maxOperations(nums1, k1)
print(f'Maximum operations for nums {nums1} with k={k1}: {result1}')  # Output: 2

# Example 2
nums2 = [3, 1, 3, 4, 3]
k2 = 6
result2 = solution.maxOperations(nums2, k2)
print(f'Maximum operations for nums {nums2} with k={k2}: {result2}')  # Output: 1

# Expected Output
"""
Maximum operations for nums [1, 2, 3, 4] with k=5: 2
Maximum operations for nums [3, 1, 3, 4, 3] with k=6: 1
"""