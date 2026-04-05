class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        b=False
        h=False

        if (length>= 10000 or width >= 10000 or height >= 10000 or length*width*height>=10**9):
            b=True
        if mass >=100:
            h=True
        if b and h :
            return "Both"
        elif b:
            return "Bulky"
        elif h:
            return "Heavy"
        else :
            return "Neither"
        