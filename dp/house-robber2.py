class Solution(object):
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]

        def rob1(houses):
            dp = [0]*len(houses)
            dp[0] = houses[0]
            if len(houses)>1:
                dp[1] = max(houses[0],houses[1])
                for i in range(2,len(houses)):
                    dp[i] = max(houses[i]+dp[i-2], dp[i-1])
            return dp[-1]
        case1 = rob1(nums[1:])
        case2 = rob1(nums[:-1])
        return max(case1,case2)            
              