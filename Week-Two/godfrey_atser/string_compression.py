class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Pointer to write the compressed characters
        read = 0   # Pointer to read the characters
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            # Count the number of occurrences of the current character
            while read < n and chars[read] == current_char:
                read += 1
                count += 1
            
            # Write the current character
            chars[write] = current_char
            write += 1
            
            # If count is more than 1, write the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write  # New length of the array


# Example Usage

# Instantiate the Solution class
solution = Solution()

# Example 1
chars1 = ["a", "a", "b", "b", "c", "c", "c"]
length1 = solution.compress(chars1)
print(length1, chars1[:length1])  # Output: 6 ['a', '2', 'b', '2', 'c', '3']

# Example 2
chars2 = ["a"]
length2 = solution.compress(chars2)
print(length2, chars2[:length2])  # Output: 1 ['a']

# Example 3
chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
length3 = solution.compress(chars3)
print(length3, chars3[:length3])  # Output: 4 ['a', 'b', '1', '2']


# Expected Output
"""
6 ['a', '2', 'b', '2', 'c', '3']
1 ['a']
4 ['a', 'b', '1', '2']
"""
