class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        i1 = 1
        i2 = 2
        for _ in range(3,n+1):
            curr = i1+i2
            i1 =i2
            i2 = curr
        return i2