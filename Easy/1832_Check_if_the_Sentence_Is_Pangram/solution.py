class Solution(object):
    def checkIfPangram(self, sentence):
        checker = set(sentence)
        return len(checker) == 26
