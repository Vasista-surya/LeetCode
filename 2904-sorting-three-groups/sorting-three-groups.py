class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # dp1=dp2=dp3=0
        # for i in nums:
        #     if i==1:
        #         dp1 +=1
        #     elif i==2:
        #         dp2=max(dp1,dp2)+1
        #     else :
        #         dp3=max(dp2,dp3)+1
        #     # ndp1=dp1+(i!=1)
        #     # ndp2=min(dp1,dp2)+(i!=2)
        #     # ndp3=min(dp2,dp3)+(i!=3)

        #     # dp1,dp2,dp3=ndp1,ndp2,ndp3

        # return len(nums) - max(dp1,dp2,dp3)
        n=len(nums)
        dp =[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<=nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        ins=max(dp)
        return n-ins
        