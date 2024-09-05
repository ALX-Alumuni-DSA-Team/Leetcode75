class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u"]
        position = []
        new_s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                position.append(i)
        for j in range(len(position)):
            new_s[position[j]] = s[position[-(j+1)]]
        return "".join(new_s)

s = "hello"
solution = Solution()
print(solution.reverseVowels(s)) 
s = "leetcode"
solution = Solution()
print(solution.reverseVowels(s))       