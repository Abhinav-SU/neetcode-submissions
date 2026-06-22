class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if m == 0:
            return 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        maxArea = 0

        def dfs(start_r,start_c):
            stack = [(start_r,start_c)]
            grid[start_r][start_c]=0
            area =1
            while stack:
                
                r,c = stack.pop()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]==1:
                        area += 1
                        grid[nr][nc] = 0
                        stack.append((nr,nc))
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(maxArea,area)

        return maxArea