class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Step 1: Find the maximum number of candies any kid currently has
        max_candies = max(candies)
        
        # Step 2: Check if each kid can have the maximum candies after receiving extraCandies
        result = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        # Step 3: Return the result list
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
