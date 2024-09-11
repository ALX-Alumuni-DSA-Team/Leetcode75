class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize two pointers
        left = 0
        right = len(height) - 1
        
        # Variable to keep track of the maximum area
        max_area = 0
        
        # Loop while left pointer is less than the right pointer
        while left < right:
            # Calculate the width between the two lines
            width = right - left
            
            # Calculate the current area (height is determined by the shorter line)
            current_area = min(height[left], height[right]) * width
            
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage

# Instantiate the Solution class
solution = Solution()

# Example 1
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result1 = solution.maxArea(height1)
print(f'Maximum water the container can store for height {height1}: {result1}')  # Output: 49

# Example 2
height2 = [1, 1]
result2 = solution.maxArea(height2)
print(f'Maximum water the container can store for height {height2}: {result2}')  # Output: 1

# Expected Output
""" 
Maximum water the container can store for height [1, 8, 6, 2, 5, 4, 8, 3, 7]: 49
Maximum water the container can store for height [1, 1]: 1
"""

