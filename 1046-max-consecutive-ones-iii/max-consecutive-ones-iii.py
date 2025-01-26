class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ZERO_COUNT = 0
        l, r = 0, 0
        MAX_LENGTH = 0
        while r < len(nums):
            if nums[r] == 0:
                ZERO_COUNT += 1
            while ZERO_COUNT > k:
                if nums[l] == 0:
                    ZERO_COUNT -= 1
                l += 1
            MAX_LENGTH = max(MAX_LENGTH, r - l + 1)
            r += 1
        return MAX_LENGTH
