class Solution(object):
    def productExceptSelf(self, nums):
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[0] = 1
        for i in range(1,len(nums)):
            left[i]= left[i-1]*nums[i-1]
        right[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        answer = [1]*len(nums)
        for i in range(len(nums)):
            answer[i] = left[i]*right[i]        
        return answer