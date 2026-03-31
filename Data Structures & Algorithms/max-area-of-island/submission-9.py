class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0

        
        def dfs(r,c):
            if r < 0 or r >= row:
                return
            if c < 0 or c >= cols:
                return
            if (r,c) in visited:
                return
            if grid[r][c]=="0":
                return
            visited.add((r,c))
            count = 0
            if grid[r+1][c] == "1" or grid[r-1][c] == "1"  or grid[r][c+1]== "1"  or grid[r][c-1]== "1" :
                count+=1
            m = count
            count = max(count,m)
        return count



