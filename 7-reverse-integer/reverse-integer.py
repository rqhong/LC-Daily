class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if x == 0:
            return 0
        
        is_p = False
        if x > 0:
            is_p = True
        
        l = []
        x = abs(x)
        while x>0:
            l.append(x % 10)
            x //= 10
            
        res = 0
        mul = 1
        for n in reversed(l):
            res += n*mul
            mul*=10
        
        if not is_p:
            res = -res

        if res < INT_MIN or res > INT_MAX:
            return 0
        return res
