class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Calculate prefix product for each element
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Calculate suffix product and multiply with the current answer
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
    
    
# Example Usage
# Instantiate the Solution class
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4]
result1 = solution.productExceptSelf(nums1)
print(f'Product except self: {result1}')  # Output: [24, 12, 8, 6]

# Example 2
nums2 = [-1, 1, 0, -3, 3]
result2 = solution.productExceptSelf(nums2)
print(f'Product except self: {result2}')  # Output: [0, 0, 9, 0, 0]

# Expected Output
"""
Product except self: [24, 12, 8, 6]
Product except self: [0, 0, 9, 0, 0]
"""