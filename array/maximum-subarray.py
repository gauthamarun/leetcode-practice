class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        maximum_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            maximum_sum = max(current_sum, maximum_sum)
        return maximum_sum    

        