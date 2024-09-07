class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_word = []
        length1 = len(word1)
        length2 = len(word2)

        for i in range(min(length1, length2)):
            merged_word.append(word1[i])
            merged_word.append(word2[i])
        
        if length1 > length2:
            merged_word.append(word1[length2:])
        else:
            merged_word.append(word2[length1:])
        return "".join(merged_word)