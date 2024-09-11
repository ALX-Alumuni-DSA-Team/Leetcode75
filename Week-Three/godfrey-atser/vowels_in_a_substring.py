class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Helper set for vowels
        vowels = set('aeiou')
        
        # Initial count of vowels in the first window of size 'k'
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        
        # Track the maximum number of vowels in any window
        max_vowels = vowel_count
        
        # Sliding window: move the window across the string
        for i in range(k, len(s)):
            # Remove the effect of the character that slides out of the window
            if s[i - k] in vowels:
                vowel_count -= 1
            # Add the effect of the character that slides into the window
            if s[i] in vowels:
                vowel_count += 1
            
            # Update the maximum count of vowels
            max_vowels = max(max_vowels, vowel_count)
        
        return max_vowels

# Instantiate the Solution class
solution = Solution()

#Example Usage

# Example 1
s1 = "abciiidef"
k1 = 3
result1 = solution.maxVowels(s1, k1)
print(f'Maximum vowels in any substring of length {k1} in "{s1}": {result1}')  # Output: 3

# Example 2
s2 = "aeiou"
k2 = 2
result2 = solution.maxVowels(s2, k2)
print(f'Maximum vowels in any substring of length {k2} in "{s2}": {result2}')  # Output: 2

# Example 3
s3 = "leetcode"
k3 = 3
result3 = solution.maxVowels(s3, k3)
print(f'Maximum vowels in any substring of length {k3} in "{s3}": {result3}')  # Output: 2

# Expected Output
"""
Maximum vowels in any substring of length 3 in "abciiidef": 3
Maximum vowels in any substring of length 2 in "aeiou": 2
Maximum vowels in any substring of length 3 in "leetcode": 2
"""