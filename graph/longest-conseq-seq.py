class Solution(object):
    def longestConsecutive(self, nums):
        seen = set(nums)
        longest = 0
        for num in seen:
            if num-1 not in seen:
                next_num = num+1
                length = 1
                while next_num in seen:
                    length+=1
                    next_num+=1
                longest = max(length, longest)
        return longest            
        