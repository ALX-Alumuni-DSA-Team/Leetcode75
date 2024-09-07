
def reverseVowels(s):
    vowels = set("aeiouAEIOU")  # Set of vowels for quick lookup
    s = list(s)  # Convert string to a list to allow in-place modification
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]  # Swap vowels
            left += 1
            right -= 1
        if s[left] not in vowels:
            left += 1
        if s[right] not in vowels:
            right -= 1
    
    return "".join(s)  # Convert list back to string

# Example usage
print(reverseVowels("Natural Language processing"))  # Output: "Niterol Lengauga pracussang"
print(reverseVowels("Classification and Regression"))  # Output: "Clossifecetaon ind Ragrissian"
