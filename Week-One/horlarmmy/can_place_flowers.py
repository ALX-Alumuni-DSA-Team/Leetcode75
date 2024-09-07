class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        bed_length = len(flowerbed)
        for i in range(bed_length):
            left_empty = (i == 0) or (flowerbed[i-1] ==0)
            right_empty = (i == bed_length - 1) or (flowerbed[i+1] == 0)

            if left_empty and right_empty and flowerbed[i] ==0:
                flowerbed[i] =1
                n-=1
        return n<=0
    
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