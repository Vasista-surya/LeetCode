class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)> len(nums2):
            nums1,nums2=nums2,nums1

        x,y=len(nums1),len(nums2)
        l,h=0,x
        while l<=h:
            px=(l+h)//2
            py=(x+y+1)//2 -px

            mlx=float('-inf') if px ==0 else nums1[px-1]
            mrx=float('inf') if px ==x else nums1[px]

            mly = float('-inf') if py == 0 else nums2[py-1]
            mry = float ('inf') if py == y else nums2[py]


            if mlx <= mry and mly <= mrx :
                if (x+y) %2 ==0:
                    return (max(mlx,mly)+ min(mrx,mry))/2.0
                else :
                    return max(mlx,mly)

            elif mlx >mry :
                h=px-1
            else :
                l=px+1