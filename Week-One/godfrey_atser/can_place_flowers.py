class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Extend the flowerbed with an additional 0 at the beginning and end
        # This helps in handling edge cases
        flowerbed = [0] + flowerbed + [0]
        
        # Iterate through the flowerbed
        for i in range(1, len(flowerbed) - 1):
            # Check if the current plot and its adjacent plots are empty
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                # Place a flower here
                flowerbed[i] = 1
                # Decrement n
                n -= 1
                # If all flowers are placed, return True
                if n == 0:
                    return True
        
        # If we have more flowers left to plant, return False
        return n <= 0

#EXAMPLE USAGE
# Example 1
flowerbed = [1, 0, 0, 0, 1]
n = 1
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))  # Output: True

# Example 2
flowerbed = [1, 0, 0, 0, 1]
n = 2
print(solution.canPlaceFlowers(flowerbed, n))  # Output: False
