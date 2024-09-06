class Solution:
    def reverseWords(self, s: str) -> str:
        output = s.strip().split()
        return ' '.join(reversed(output))


if __name__ == '__main__':
    obj = Solution()
    my_str = "a good   example"
    out = obj.reverseWords(my_str)
    print(out)
