class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        t = []
        t.append(0) # t0
        t.append(1) # t1
        t.append(1) # t2
        for i in range(n-2):
            t.append(sum(t[i:i+3]))
        
        return t[-1] 