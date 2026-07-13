class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        r=[]
        s="123456789"
        for length in range(len(str(low)),len(str(high))+1):
            for i in range(10-length):
                num=int(s[i:i+length])
                if low <=num<=high:
                    r.append(num)
        return r
