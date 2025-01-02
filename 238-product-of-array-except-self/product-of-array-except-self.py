class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        zero_count = nums.count(0)
        if zero_count ==1:
            total_product = 1
            for num in nums:
                if num != 0:
                    total_product *= num
            
            zero_index = nums.index(0)
            for i in range(len(nums)):
                nums[i] = 0
            nums[zero_index] = total_product
            

        elif zero_count > 1:
            for i in range(len(nums)):
                nums[i] = 0

        else:
            a = 1
            for n in nums:
                a *= n
            for i in range(len(nums)):
                nums[i] = a / nums[i]

        return nums            