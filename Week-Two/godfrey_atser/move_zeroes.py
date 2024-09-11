class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0  # Pointer to place the next non-zero element

        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[non_zero_index] = num
                non_zero_index += 1
        
        # Fill the remaining array with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

# Example Usage

# Instantiate the Solution class
solution = Solution()

# Example 1
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

# Example 2
nums2 = [0]
solution.moveZeroes(nums2)
print(nums2)  # Output: [0]


# Expected Solution
"""
[1, 3, 12, 0, 0]
[0]
"""
