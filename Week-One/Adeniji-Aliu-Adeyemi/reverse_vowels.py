class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #lookup vowels
        vowels = set("aeiouAEIOU")

        #convert the user input to a list
        s = list(s)

        # set pointers from left and right
        left, right = 0, len(s) - 1

        while left < right:
            #if vowels are found from left and right
            if s[left] in vowels and s[right] in vowels:
                #swap the vowel letters
                s[left], s[right] = s[right],s[left]
                left +=1
                right -=1
            
            if s[left] not in vowels:
                left +=1
            if s[right] not in vowels:
                right -=1

        return "".join(s)

#Example
solution = Solution()
print(solution.reverseVowels("hello"))    # Output: "holle"
print(solution.reverseVowels("leetcode")) # Output: "leotcede"

        







