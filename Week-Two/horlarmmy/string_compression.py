class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        i = 0
        while i < len(chars):
            current = chars[i]
            count = 0
            while i < len(chars) and chars[i] == current:
                count += 1
                i += 1
            chars[write] = current
            write +=1 
            if count> 1:
                for num in str(count):
                    chars[write] = num
                    write += 1

        return write
chars = ["a","a","b","b","c","c","c"]
result = Solution()
out = result.compress(chars)
print(out)
