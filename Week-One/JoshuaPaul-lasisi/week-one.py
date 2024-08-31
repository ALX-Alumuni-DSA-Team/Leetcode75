# Question 1
def mergeAlternately(word1: str, word2: str) -> str:
    merged_string = []
    i, j = 0, 0
    
    # Add letters in alternating order
    while i < len(word1) and j < len(word2):
        merged_string.append(word1[i])
        merged_string.append(word2[j])
        i += 1
        j += 1
    
    # Append remaining letters from the longer string
    if i < len(word1):
        merged_string.append(word1[i:])
    if j < len(word2):
        merged_string.append(word2[j:])
    
    return ''.join(merged_string)

# Execution
print('--------')
print('Question 1')
print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))
print(mergeAlternately("abcd", "pq")) 



# Question 2
import math

def gcdOfStrings(str1: str, str2: str) -> str:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    gcd_length = gcd(len(str1), len(str2))
    gcd_string = str1[:gcd_length]
    
    if gcd_string * (len(str1) // gcd_length) == str1 and gcd_string * (len(str2) // gcd_length) == str2:
        return gcd_string
    return ""

# Execution
print('--------')
print('Question 2')
print(gcdOfStrings("ABCABC", "ABC")) 
print(gcdOfStrings("ABABAB", "ABAB"))
print(gcdOfStrings("LEET", "CODE"))



# Question 3
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    result = [candy + extraCandies >= max_candies for candy in candies]
    return result

# Execution
print('--------')
print('Question 3')
print(kidsWithCandies([2, 3, 5, 1, 3], 3))
print(kidsWithCandies([4, 2, 1, 1, 2], 1)) 
print(kidsWithCandies([12, 1, 12], 10))




# Question 4
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
            if count >= n:
                return True
    return count >= n

# Execution
print('--------')
print('Question 4')
print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(canPlaceFlowers([1, 0, 0, 0, 1], 2)) 




# Question 5
def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
    return ''.join(s_list)

# Execution
print('--------')
print('Question 5')
print(reverseVowels("hello")) 
print(reverseVowels("leetcode"))
