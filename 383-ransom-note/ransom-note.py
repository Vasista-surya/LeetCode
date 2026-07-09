class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote :
            if ransomNote.count(char)>magazine.count(char):
                return False
        return True  