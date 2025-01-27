class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        res = [0] * len(spells)
        potions = sorted(potions)
        
        for i, s in enumerate(spells):
            l, r = 0, len(potions)
            while l < r :
                m = (l+r) // 2
                if s * potions[m] >= success:
                    r = m
                else:
                    l = m + 1
            res[i] = len(potions) - l

        return res