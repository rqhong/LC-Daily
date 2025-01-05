class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))
        return res