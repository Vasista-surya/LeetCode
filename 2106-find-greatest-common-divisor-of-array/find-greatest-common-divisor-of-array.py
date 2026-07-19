class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        # while b:
        #     a,b=b,a%b
        c=gcd(a,b)
        return c