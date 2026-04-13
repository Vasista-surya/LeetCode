class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        
        mind=float('inf')
        for i in range (len(nums)):
            if nums[i]==target:
                mind=min(mind,abs(i-start))
        return mind