class Solution(object):
    def fib(self, n):
        #base case
        if n==0:
            return 0
        if n==1:
            return 1
        #recursive case
        else:
            return self.fib(n-1)+self.fib(n-2)
