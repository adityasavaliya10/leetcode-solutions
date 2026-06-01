class Solution(object):
    def mostWordsFound(self, sentences):
        max = 0
        for sentence in sentences:
            words = len(sentence.split())

            if words > max:
                max = words

        return max          
