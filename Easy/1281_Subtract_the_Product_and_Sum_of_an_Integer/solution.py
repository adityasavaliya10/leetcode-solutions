class Solution(object):
    def subtractProductAndSum(self, n):
        
        temp = n
        sum = 0
        while temp>0:
            r = temp%10
            sum +=r
            temp//=10


        temp = n 
        product = 1

        while temp>0:
            r = temp%10
            product = product*r
            temp//=10


        return product - sum
