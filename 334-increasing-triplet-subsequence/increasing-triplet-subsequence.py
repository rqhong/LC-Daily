class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = float('inf')
        smaller = float('inf')

        for i in range(len(nums)):
            
            if nums[i] <= smallest:
                smallest = nums[i]
            elif nums[i] <= smaller:
                smaller = nums[i]
            else:
                return True
        
        return False


                