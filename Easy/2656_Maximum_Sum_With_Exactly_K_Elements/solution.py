class Solution(object):
    def maximizeSum(self, nums, k):
        maximum = max(nums)
        total = 0

        for i in range(k):
            total += maximum
            maximum += 1

        return total
