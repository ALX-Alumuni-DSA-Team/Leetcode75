def mergeAlternately(word1: str, word2: str) -> str:
    merged_string = []
    len1, len2 = len(word1), len(word2)
    
    # Iterate over both strings up to the length of the shorter one
    for i in range(min(len1, len2)):
        merged_string.append(word1[i])
        merged_string.append(word2[i])
    
    # Append the remaining part of the longer string
    if len1 > len2:
        merged_string.append(word1[len2:])
    else:
        merged_string.append(word2[len1:])
    
    return ''.join(merged_string)

# Test cases
print(mergeAlternately("abc", "pqr"))   # Output: "apbqcr"
print(mergeAlternately("ab", "pqrs"))   # Output: "apbqrs"
print(mergeAlternately("abcd", "pq"))   # Output: "apbqcd"
