class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0

        count = 0
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
            if dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1):
                count+=1
            m = count
            count = max(count,m)
        return count



