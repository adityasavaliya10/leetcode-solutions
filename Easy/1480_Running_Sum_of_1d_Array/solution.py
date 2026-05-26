class Solution(object):
    def runningSum(self, nums):
        sum = []
        a = 0
        for i in nums:
            a += i
            sum.append(a)
        return sum
