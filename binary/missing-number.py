class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = (n*(n+1))/2
        curr_sum = 0
        for i in range(n):
            curr_sum = curr_sum + nums[i]
        return total-curr_sum    