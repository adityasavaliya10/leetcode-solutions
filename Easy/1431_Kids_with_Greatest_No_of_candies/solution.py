class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxC = max(candies)
        ans = []
        for i in candies:
            if i+extraCandies>=maxC:
                ans.append(True)
            else:
                ans.append(False)
        return ans

