class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = -float('inf')
        # left string should have the most zeros
        for i in range(1, len(s)):
            m = max(m, s[:i].count('0') + s[i:].count('1'))

        return m
            