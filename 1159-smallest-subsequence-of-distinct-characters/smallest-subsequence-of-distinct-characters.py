class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        l={}
        for i in range(len(s)):
            l[s[i]]=i
        stack=[]
        seen=set()
        for i in range(len(s)):
            if s[i] in seen :
                continue
            while stack and stack[-1]>s[i] and l[stack[-1]]>i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)