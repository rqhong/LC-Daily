class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from heapq import *

        heap = []
        heapify(heap)

        for n in nums:
            heappush(heap, n)
        
        m = len(heap) - k + 1 
        for i in range(m):
            r = heappop(heap)

        return r