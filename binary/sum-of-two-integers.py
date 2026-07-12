class Solution(object):
    def getSum(self, a, b):
        sum_without_carry = a^b
        carry = (a&b)<<1
        return sum_without_carry + carry