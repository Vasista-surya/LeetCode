class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        group =[0]*n
        for i in range(1,n):
            group[i]=group[i-1]
            if nums[i]-nums[i-1]>maxDiff:
                group[i]+=1
        return [group[u]==group[v] for u,v in queries]