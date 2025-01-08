class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        count = 0
        keys = list(d.keys())

        for key in keys:
            completion = k - key
            if completion == key:
                count += d[key] // 2
                d[key] -= 2 * count
            else:
                subs = min(d[key], d[completion])
                count += subs
                d[key], d[completion] = d[key]-subs, d[completion]-subs

        return count