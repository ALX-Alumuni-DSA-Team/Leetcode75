class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Calculate the sum of the first 'k' elements
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window through the array
        for i in range(k, len(nums)):
            # Update the window sum by adding the new element and removing the old one
            window_sum += nums[i] - nums[i - k]
            # Track the maximum sum
            max_sum = max(max_sum, window_sum)
        
        # Return the maximum average
        return float(max_sum) / k

# Instantiate the Solution class
solution = Solution()


# Example Usage
# Example 1
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
result1 = solution.findMaxAverage(nums1, k1)
print(f'Maximum average for nums {nums1} with k={k1}: {result1:.5f}')  # Output: 12.75000

# Example 2
nums2 = [5]
k2 = 1
result2 = solution.findMaxAverage(nums2, k2)
print(f'Maximum average for nums {nums2} with k={k2}: {result2:.5f}')  # Output: 5.00000

# Expected Output
"""
Maximum average for nums [1, 12, -5, -6, 50, 3] with k=4: 12.75000
Maximum average for nums [5] with k=1: 5.00000
"""