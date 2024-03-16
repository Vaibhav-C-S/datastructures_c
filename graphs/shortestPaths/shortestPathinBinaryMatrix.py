from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distance = [[float("inf")] * n for _ in range(n)]
        queue= deque()
        if grid[0][0] != 0 :
            return -1
        queue.append((0,0))
        distance[0][0]= 1
        while queue:
            curr_i,curr_j = queue.popleft()
            for i in range(-1,2):
                for j in range(-1,2):
                    new_i = curr_i + i
                    new_j = curr_j + j
                    if (0<=new_i<n) and (0<=new_j<n) and grid[new_i][new_j] == 0:
                        if distance[curr_i][curr_j] + 1  < distance[new_i][new_j]:
                            distance[new_i][new_j] = distance[curr_i][curr_j] + 1
                            queue.append((new_i,new_j))
        if distance[n-1][n-1] == float("inf"):return -1
        return distance[n-1][n-1]
        
