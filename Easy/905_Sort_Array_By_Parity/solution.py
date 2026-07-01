class Solution(object):
    def sortArrayByParity(self, nums):
      even = []
      odd = []

      for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

      s = even + odd
      return s
