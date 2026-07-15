# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
class Solution(object):
    def getSum(self, a, b):
        sum_without_carry = a^b
        carry = (a&b)<<1
        return sum_without_carry + carry