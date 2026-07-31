# not dp solution
#dp solution exceeds time limit

class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        goal = n-1
        for i in range(n-1,-1,-1):
            if nums[i]+i>=goal:
                goal=i
        return goal == 0        

