class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        Island=0
        Visit=set()
        ROWS,COLS=len(grid),len(grid[0])


        def bfs(r,c):
            q=collections.deque()
            Visit.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.popleft()
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if (row in range(ROWS) and col in range(COLS) and 
                        grid[row][col]=="1" and (row,col) not in Visit):
                        Visit.add((row,col))
                        q.append((row,col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in Visit:
                    bfs(r,c)
                    Island+=1
        return Island