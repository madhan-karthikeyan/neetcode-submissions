class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            area = 1
            q = deque()
            grid[r][c] = 0
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]==0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]=0
                    area+=1
            
            return area
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    maxArea = max(maxArea, bfs(i,j))
        
        return maxArea