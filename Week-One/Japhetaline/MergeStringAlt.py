class Solution(object):
    def mergeAlternately(self, wrdOne, wrdTwo):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p = len(wrdOne)
        q = len(wrdTwo)
        r = 0
        t = 0
        outcome = []

        while r < p or t < q:
            if r < p:
                outcome += wrdOne[r] 
                r += 1
            if t < q:
                outcome += wrdTwo[t]
                t += 1

        return "".join(outcome)
