class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #function to determine the greatest common divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
    
        #checking to confirm the strings could be allowed for gcd test
        if str1+str2 !=str2+str1:
            return ""
        else:
            gcd_length = gcd(len(str1),len(str2))   #The gcd is stored
            return str1[:gcd_length]    #The greatest common string is gotten
#Instance of of the class
solution = Solution()
#Test Cases
print(solution.gcdOfStrings("ABCABC","ABC"))    #Expected Output: ABC
print(solution.gcdOfStrings("ABABAB","ABAB"))   #Expected Output: AB
print(solution.gcdOfStrings("LEET","CODE"))     #Expected Output: ""
print(solution.gcdOfStrings("ABCDEF","ABC"))    #Expected Output: ""