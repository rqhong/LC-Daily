class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        FLIP = False
        f_idx = 0
        l, r = 0, 0
        max_l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if FLIP: # 等於零且被翻過
                    l = f_idx + 1
                FLIP = True
                f_idx = r # f_idx 都必須被記錄到
            max_l = max(max_l, r-l)
        max_l = max(max_l, r-l)
        return max_l