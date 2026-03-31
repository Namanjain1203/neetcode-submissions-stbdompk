class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        i = 1
        j = 2
        for _ in range(3,n+1):
            curr = i+j
            i=j
            j=curr
        return j