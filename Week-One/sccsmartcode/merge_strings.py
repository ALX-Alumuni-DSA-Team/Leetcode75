class Solution(object):
    def mergeAlternately(self, word1, word2):
        index = 0
        output = ""

        while index < len(word1) or index < len(word2):
            if index < len(word1):
                output += word1[index]
            if index < len(word2):
                output += word2[index]
            index += 1
        return output
