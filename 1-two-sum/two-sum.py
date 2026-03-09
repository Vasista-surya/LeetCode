class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num={}
        for i in range(len(nums)):
            complement =target-nums[i]
            if complement in num:
                return [num[complement],i]
            num[nums[i]]=i
        