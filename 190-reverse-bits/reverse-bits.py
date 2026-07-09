class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=0
        for i in range(32):
            r = r*2+n%2
            n=n//2
        return r