class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_string = ""
        i, j = 0, 0
        n, m = len(word1), len(word2)
        
        # Loop through both strings while adding characters alternately
        while i < n and j < m:
            merged_string += word1[i] + word2[j]
            i += 1
            j += 1
        
        # Append remaining characters of the longer string
        if i < n:
            merged_string += word1[i:]
        if j < m:
            merged_string += word2[j:]
        
        return merged_string

#EXAMPLE USAGE

# Example 1:
word1 = "abc"
word2 = "pqr"
# Output: "apbqcr"
# Explanation:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
solution = Solution()
print(solution.mergeAlternately(word1, word2))  # Expected output: "apbqcr"

# Example 2:
word1 = "ab"
word2 = "pqrs"
# Output: "apbqrs"
# Explanation:
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q r s
print(solution.mergeAlternately(word1, word2))  # Expected output: "apbqrs"

# Example 3:
word1 = "abcd"
word2 = "pq"
# Output: "apbqcd"
# Explanation:
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c d
print(solution.mergeAlternately(word1, word2))  # Expected output: "apbqcd"
