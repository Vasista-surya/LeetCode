class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        pa= { ')' : '(' , '}' : '{' , ']' : '['}

        for char in s :
            if char in "({[":
                st.append(char)
            else :
                if not st or st[-1] != pa[char]:
                    return False
                st.pop()
        return len(st) == 0
        