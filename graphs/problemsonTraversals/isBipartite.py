from collections import deque
class Solution:
    def bfs(self,node,graphs,colors):
        queue = deque()
        queue.append((node,0))
        while queue:
            node,color = queue.popleft()
            for neighbour in graphs[node]:
                if colors[neighbour] == -1:
                    next_color = 1 - color
                    colors[neighbour] = next_color
                    queue.append((neighbour,next_color))
                elif colors[neighbour] == color:
                    return False 
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1] * V 
        for i in range(V):
            if colors[i] == -1:
                if self.bfs(i,graph,colors) == False:
                    return False 
        return True


-----------------------------------------------------------------------------------------------------------------------------
from collections import deque
class Solution:
    def dfs(self,node,graphs,colors,color):
        colors[node] = color
        for neighbour in graphs[node]:
            if colors[neighbour] == -1:
                if self.dfs(neighbour,graphs,colors,1-color) == False:
                    return False 
            elif colors[neighbour] == color:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1] * V 
        for i in range(V):
            if colors[i] == -1:
                if self.dfs(i,graph,colors,0) == False:
                    return False 
        return True


        
