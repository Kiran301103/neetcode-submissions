class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit=set()
        Island=0
        ROWS,COLS=len(grid),len(grid[0])


        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.popleft()
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if(r in range(ROWS) and c in range(COLS) and
                        grid[r][c]=="1" and (row,col) not in visit):
                        visit.add((row,col))
                        q.append((row,col))                        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    Island+=1
        return Island    

        
            