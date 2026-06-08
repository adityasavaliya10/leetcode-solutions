class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        last = words[-1]
        length = len(last)

        return length
