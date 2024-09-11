class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """  
        s = s.strip().split()
        return " ".join(reversed(s))

s = "the sky is blue"

result = Solution()
out = result.reverseWords(s)
print(out)
s = "  hello world  "
out = result.reverseWords(s)
print(out)
s = "a good   example"
out = result.reverseWords(s)
print(out)