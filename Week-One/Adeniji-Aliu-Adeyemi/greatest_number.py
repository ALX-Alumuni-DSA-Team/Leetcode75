class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        #initialize an empty list
        result = []
        #get a new candy list 
        new_candies = list(map(lambda x: x+extraCandies, candies))
        #loop through the new candies and compare with max of the old candies
        for candy in new_candies:
            if candy >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result

#EXAMPLE USAGE
# Example 1
candies = [2, 3, 5, 1, 3]
extraCandies = 3
solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]

# Example 2
candies = [4, 2, 1, 1, 2]
extraCandies = 1
print(solution.kidsWithCandies(candies, extraCandies))  # Output: [True, False, False, False, False]

# Example 3
candies = [12, 1, 12]
extraCandies = 10
print(solution.kidsWithCandies(candies, extraCandies))  # Output: [True, False, True]