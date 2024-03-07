from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    fresh+=1
        row_i = [-1,0,1,0]
        col_j = [0,1,0,-1]
        maxtime = 0

        while queue:
            curr_i,curr_j,time = queue.popleft()
            maxtime = max(time,maxtime)
            for i in range(4):
                new_i = curr_i + row_i[i]
                new_j = curr_j + col_j[i]
                if (0<=new_i<m) and (0<=new_j<n) and grid[new_i][new_j] == 1 :
                    grid[new_i][new_j] = 2
                    fresh-=1
                    queue.append((new_i,new_j,time+1))
        
        if fresh>0:return -1
        return maxtime
                    


