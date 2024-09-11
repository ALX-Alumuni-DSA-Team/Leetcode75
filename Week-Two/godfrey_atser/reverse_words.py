class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Split the string into words, automatically handling multiple spaces
        words = s.split()
        
        # Step 2: Reverse the list of words
        words.reverse()
        
        # Step 3: Join the reversed words with a single space
        return ' '.join(words)


# Usage Example

# Instantiate the Solution class
solution = Solution()

# Example 1
s1 = "the sky is blue"
result1 = solution.reverseWords(s1)
print(f'Reversed words: "{result1}"')  # Output: "blue is sky the"

# Example 2
s2 = "  hello world  "
result2 = solution.reverseWords(s2)
print(f'Reversed words: "{result2}"')  # Output: "world hello"

# Example 3
s3 = "a good   example"
result3 = solution.reverseWords(s3)
print(f'Reversed words: "{result3}"')  # Output: "example good a"

# Expected Output
"""
Reversed words: "blue is sky the"
Reversed words: "world hello"
Reversed words: "example good a"
"""
