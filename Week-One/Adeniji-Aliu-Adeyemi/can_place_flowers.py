class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        #if no flower was planted
        if n==0:
            return True
        # Begin with the first plot
        count = 0
        # check each flowerbed 
        while count < len(flowerbed):
            # Check if there are non-adjacent flowers
            if flowerbed[count] == 0:
                check_left = (count == 0 or flowerbed[count-1] == 0) 
                check_right = (count == len(flowerbed) - 1 or flowerbed[count+1] == 0) 

                if check_left and check_right:
                    # Plant a flower here
                    flowerbed[count] = 1
                    n -= 1  # Reduce the no of flower by 1

                    # If flowers are completely planted
                    if n == 0:
                        return True
                    # Skip the next plot to avoid planting adjacent flowers
                    count += 1
            # Move to the next plot
            count += 1
        # If we've planted all the required flowers
        return n==0

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

# Example 3
flowerbed = [0,0,0,0,0,1,0,0]
n=0
print(solution.canPlaceFlowers(flowerbed, n))  # Output: True