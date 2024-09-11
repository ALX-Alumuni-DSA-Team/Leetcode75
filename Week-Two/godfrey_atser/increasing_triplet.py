class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')  # Initialize first to infinity
        second = float('inf') # Initialize second to infinity

        for num in nums:
            if num <= first:
                first = num  # Update first if the current number is smaller
            elif num <= second:
                second = num  # Update second if the current number is smaller than second
            else:
                # We found a number greater than both first and second
                return True
        
        return False  # If no triplet found

# Example Usage

# Instantiate the Solution class
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4, 5]
result1 = solution.increasingTriplet(nums1)
print(f'Increasing triplet exists: {result1}')  # Output: True

# Example 2
nums2 = [5, 4, 3, 2, 1]
result2 = solution.increasingTriplet(nums2)
print(f'Increasing triplet exists: {result2}')  # Output: False

# Example 3
nums3 = [2, 1, 5, 0, 4, 6]
result3 = solution.increasingTriplet(nums3)
print(f'Increasing triplet exists: {result3}')  # Output: True


# Expected Output
"""
Increasing triplet exists: True
Increasing triplet exists: False
Increasing triplet exists: True
"""