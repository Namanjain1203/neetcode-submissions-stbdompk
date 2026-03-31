class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0
        max_area = 0
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
            if dfs(r+1,c):
                count +=1
            if dfs(r-1,c):
                count+=1
            if dfs(r,c+1):
                count +=1
            if dfs(r,c-1):
                count+=1
            count = max(count,max_row)
        for r in range(row):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    island+=1
                    dfs(r,c)
        return count

