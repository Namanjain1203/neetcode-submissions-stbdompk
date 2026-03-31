class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n -1 
        area = 0
        while i <j:
            width = j -i
            height = min(height[i],height[j])
            area = max(area,height*width)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area