class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # Handle empty array
            return -1  # Return -1 or raise an exception if no peak exists.

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:  # Peak is on the left side or at m
                r = m
            else:  # Peak is on the right side
                l = m + 1

        return l