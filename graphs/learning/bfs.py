from typing import List
from queue import Queue

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        queue = Queue()
        bfs = []
        queue.put(0)
        visited = set()
        visited.add(0)
        while not queue.empty():
          node = queue.get()
          bfs.append(node)
          for i in adj[node]:
              if i not in visited:
                  visited.add(i)
                  queue.put(i)
    
        return bfs


-----------
def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        adjMatrix = [[0]*V for _ in range(V)]
        for i in range(V):
            for j in adj[i]:
                adjMatrix[i][j] = 1 
        
        queue = Queue()
        queue.put(0)
        bfs = []
        visited = set()
        visited.add(0)
        while not queue.empty():
            node = queue.get()
            bfs.append(node)
            for neighbour in range(V):
                if adjMatrix[node][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    queue.put(neighbour)
        
        return bfs

