class Solution(object):
    def plusOne(self, digits):
        number = int("".join(map(str, digits)))
        number += 1
        return [int(i) for i in str(number)]
