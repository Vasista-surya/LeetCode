class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n=len(intervals)
        co=[False]*n
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if (intervals[j][0] <= intervals[i][0] and intervals[j][1]>= intervals[i][1]):
                        co[i]=True
                        break
        return co.count(False)