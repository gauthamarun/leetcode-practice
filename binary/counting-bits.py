class Solution(object):
    def countBits(self, n):
        dp = [0]*(n+1)
        for i in range(1,n+1):
            x = i&(i-1)
            dp[i] = dp[x]+1
        return dp          