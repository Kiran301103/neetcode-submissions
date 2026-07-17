class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visits=set()
        island=0
        rows,cols=len(grid),len(grid[0])

        def bfs(r,c):
            q=collections.deque()
            visits.add((r,c))
            q.append((r,c))
            
            while q:
                row,col=q.popleft()
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if (row in range(rows) and
                        col in range(cols) and 
                        grid[row][col]=="1" and 
                        (r,c) not in visits):
                        q.append((r,c))
                        visits.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visits:
                    bfs(r,c)
                    island+=1
        return island