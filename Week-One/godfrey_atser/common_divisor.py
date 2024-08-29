class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Check if str1 + str2 is the same as str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor of the lengths of the two strings
        gcd_length = gcd(len(str1), len(str2))
        
        # The largest string x that divides both str1 and str2
        return str1[:gcd_length]


#EXAMPLE USAGE

# Example 1:
str1 = "ABCABC"
str2 = "ABC"
# Output: "ABC"
# Explanation:
# "ABC" is the largest string that can be repeated to form both str1 and str2.
solution = Solution()
print(solution.gcdOfStrings(str1, str2))  # Expected output: "ABC"

# Example 2:
str1 = "ABABAB"
str2 = "ABAB"
# Output: "AB"
# Explanation:
# "AB" is the largest string that can be repeated to form both str1 and str2.
print(solution.gcdOfStrings(str1, str2))  # Expected output: "AB"

# Example 3:
str1 = "LEET"
str2 = "CODE"
# Output: ""
# Explanation:
# There is no common string that can be repeated to form both str1 and str2.
print(solution.gcdOfStrings(str1, str2))  # Expected output: ""
