class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        while i<j:
            mid = i+j//2
            hours = 0
            for pile in piles:
                hours+=(pile+mid-1)//mid
            if hours<=h:
                j = mid
            else:
                i = mid+1