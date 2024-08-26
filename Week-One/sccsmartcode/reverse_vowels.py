class Solution(object):
    def reverseVowels(self, s):
        vowels_str = 'aeiouAEIOU'
        s_vowels = [x for x in s if x in vowels_str]
        output = ""

        for letter in s:
            if letter in vowels_str:
                output += s_vowels[-1]
                s_vowels.pop()
            else:
                output += letter
        return output
