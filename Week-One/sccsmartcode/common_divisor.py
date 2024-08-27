class Solution(object):
    def gcdOfStrings1(self, str1, str2):
        output = ""

        for index in range(len(str1)):
            count1 = str1.count(output)
            count2 = str2.count(output)
            if output and count2 == len(str2)/len(output) and count1 == len(str1)/len(output):
                max_ = max(count1, count2)
                divisor = min_ = min(count1, count2)
                while divisor > 0:
                    if max_ % divisor == 0 and min_ % divisor == 0:
                        return output*divisor
                    divisor -= 1
            elif index < len(str2) and str1[index] == str2[index]:
                output += str1[index]
            else:
                return ""
        return output
