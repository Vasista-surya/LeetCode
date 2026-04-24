class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        mod=10**9+7
        def sersum(a,b):
            return (a+b)*(b-a+1)//2
        mid =target//2
        if n<= mid:
            return sersum(1,n)%mod
        fpart=sersum(1,mid)
        rem=n-mid
        spart=sersum(target,target+rem-1)
        return (fpart+spart)%mod
