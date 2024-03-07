from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self,node,adj,visited,parent):
        visited.add(node)
        for neighbour in adj[node]:
            if neighbour not in visited:
                if self.dfs(neighbour,adj,visited,node):
                    return True
            elif  neighbour != parent :
                return True 
        return False
                
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		V = len(adj)
		visited = set()
		for i in range(V):
		    if i not in visited:
		        if self.dfs(i,adj,visited,None) == True:
		            return 1 
		return 0

