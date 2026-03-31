class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        island = 0
        seen = set()
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col:
                return 
            if (r,c) in seen:
                return
            if dfs[r,c] =="0":
                return
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            for r in range(row):
                for c in range(col):
                    if dfs[r,c] =="1" and (r,c) not in seen:
                        island +=1
                        dfs(r,c)
            return island