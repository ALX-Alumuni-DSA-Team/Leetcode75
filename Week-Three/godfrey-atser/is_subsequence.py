class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Two pointers: one for s and one for t
        s_pointer = 0
        t_pointer = 0
        
        # Traverse through t, and try to match characters in s
        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:  # Match found
                s_pointer += 1
            t_pointer += 1
        
        # If s_pointer reached the end of s, then all characters in s are found in t
        return s_pointer == len(s)
    
    
    # Example usage
# Instantiate the Solution class
solution = Solution()

# Example 1
s1 = "abc"
t1 = "ahbgdc"
result1 = solution.isSubsequence(s1, t1)
print(f'Is "{s1}" a subsequence of "{t1}"? {result1}')  # Output: True

# Example 2
s2 = "axc"
t2 = "ahbgdc"
result2 = solution.isSubsequence(s2, t2)
print(f'Is "{s2}" a subsequence of "{t2}"? {result2}')  # Output: False



#Expected output
"""
Is "abc" a subsequence of "ahbgdc"? True
Is "axc" a subsequence of "ahbgdc"? False
"""
