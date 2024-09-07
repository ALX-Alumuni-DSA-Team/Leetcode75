class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        result = []

        for i in range(len(candies)):
            result.append((candies[i] + extraCandies) >= max_candies)
        
        return result