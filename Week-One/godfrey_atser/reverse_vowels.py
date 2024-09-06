class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Define the set of vowels (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")
        
        # Convert the string to a list to modify it in-place
        s_list = list(s)
        
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer forward until it points to a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move the right pointer backward until it points to a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            # Move both pointers
            left += 1
            right -= 1
        
        # Convert the list back to a string and return it
        return "".join(s_list)

#EXAMPLE USAGE

# Example 1
s = "hello"
solution = Solution()
print(solution.reverseVowels(s))  # Output: "holle"

# Example 2
s = "leetcode"
print(solution.reverseVowels(s))  # Output: "leotcede"
