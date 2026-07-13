class Solution(object):
    def hammingWeight(self, n):
        binary = bin(n)[2:]
        result = 0
        for ch in binary:
            if ch=='1':
                result+=1
        return result        