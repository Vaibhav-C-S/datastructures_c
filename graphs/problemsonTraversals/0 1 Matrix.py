from collections import deque
class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        distance =[[0]*n for _ in range(m)]
        visited = [ [False] *n for _ in range(m)]
        queue =  deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
                    visited[i][j] = True
                    distance[i][j]=0

        row_i = [-1,0,1,0]
        col_j = [0,1,0,-1]
        while queue:
            curr_i,curr_j,time =  queue.popleft()
            for i in range(4):
                new_i = curr_i + row_i[i]
                new_j = curr_j + col_j[i]
                if (0<=new_i<m) and (0<=new_j<n) and not visited[new_i][new_j]:
                    visited[new_i][new_j] = True
                    queue.append((new_i,new_j,time+1))
                    distance[new_i][new_j] = time+1
        return distance

       
