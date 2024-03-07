from collections import deque
class Solution:
    def bfs(self,grid,visited,i,j,m,n):
        queue = deque()
        queue.append((i,j))
        row_i = [-1,0,1,0]
        col_j = [0,1,0,-1]
        visited[i][j] = True
        while queue:
            curr_i,curr_j =queue.popleft() 
            for i in range(4):
                new_i = curr_i + row_i[i]
                new_j = curr_j + col_j[i]
                if (0<=new_i<m) and (0<=new_j<n) and grid[new_i][new_j] == "1" and not visited[new_i][new_j]:
                    visited[new_i][new_j] = True
                    queue.append((new_i,new_j)) 

        
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count=0
        visited = [ [False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.bfs(grid,visited,i,j,m,n)
                    count+=1
        return count
        
