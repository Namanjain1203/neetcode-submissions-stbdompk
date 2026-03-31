class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
            if grid[r][r]==0:
                return
            visited.add(r,c)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(row):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    island+=1
                    dfs(r,c)
        return island