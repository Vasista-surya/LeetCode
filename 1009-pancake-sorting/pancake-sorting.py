class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(arr)
        for size in range (n,1,-1):
            max=arr.index(size)
            if max!=0:
                self.flip(arr,max+1)
                res.append(max+1)

            self.flip(arr,size)
            res.append(size)
        return res

    def flip(self,arr,k):
        arr[:k]=arr[:k][::-1]
        