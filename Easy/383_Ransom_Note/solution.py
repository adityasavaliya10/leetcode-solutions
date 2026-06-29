class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for x in ransomNote:
            if ransomNote.count(x) > magazine.count(x):
                return False
            else:
                return True
        
