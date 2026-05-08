class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        i = 0
        j = n-1
        while i<j:
            area = min(heights[i],heights[j]) * (j-i)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            max_area =max(area,max_area)
        return max_area
            