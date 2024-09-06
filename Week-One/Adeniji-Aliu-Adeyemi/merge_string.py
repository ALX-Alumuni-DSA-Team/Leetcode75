class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        length = min(len(word1),len(word2))
        for i in range(length):
            merged.append(word1[i])
            merged.append(word2[i])
        if len(word1) > len(word2):
            merged.append(word1[length:])
        else:
            merged.append(word2[length:])
        return "".join(merged)
        