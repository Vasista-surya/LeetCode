class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        r=len(matrix)
        c=len(matrix[0])

        for i in range(1,r):
            for j in range(c):
                if matrix [i][j]==1:
                    matrix[i][j]+=matrix[i-1][j]

        maxa=0

        for i in range(r):
            h=sorted(matrix[i],reverse=True)
            for j in range(c):
                area=h[j]*(j+1)
                maxa=max(maxa,area)
        return  maxa

