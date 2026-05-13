class Solution(object):
    def countDigits(self, num):
        temporary = num
        count = 0

        while temporary > 0:
            r = temporary % 10

            if num % r == 0:
                count += 1

            temporary //= 10

        return count
