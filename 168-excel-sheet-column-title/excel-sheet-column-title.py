class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        r=""
        while columnNumber >0:
            columnNumber -=1
            r=chr(columnNumber% 26+ord('A'))+r
            columnNumber//=26
        return r