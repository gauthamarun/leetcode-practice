#container with most water
class Solution(object):
    def maxArea(self, height):
        l,r = 0, len(height)-1
        max_area = 0
        while l<r:
            if height[l]<height[r]:
                curr_area = height[l]*(r-l)
                max_area = max(curr_area, max_area)
                l+=1
            elif height[l]>height[r]:
                curr_area = height[r]*(r-l)
                max_area = max(curr_area, max_area)
                r-=1
            else:
                curr_area = height[r]* (r-l)
                max_area = max(curr_area, max_area)  
                l+=1
                r-=1        
        return max_area