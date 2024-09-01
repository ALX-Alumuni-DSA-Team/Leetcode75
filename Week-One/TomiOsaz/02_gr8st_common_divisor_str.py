import math

def gcdOfStrings(str1, str2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def check(x):
        return str1 == x * (len(str1) // len(x)) and str2 == x * (len(str2) // len(x))
    
    length_gcd = gcd(len(str1), len(str2))
    candidate = str1[:length_gcd]
    return candidate if check(candidate) else ""

# Trial Run
print(gcdOfStrings("TOMTOM", "TOM"))  # Output: "TOM"
