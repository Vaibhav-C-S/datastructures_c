#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def dfs(self,node,adj,visited,pathvisited):
        visited.add(node)
        pathvisited.add(node)
        for neighbour in adj[node]:
            if neighbour not in visited:
                if self.dfs(neighbour,adj,visited,pathvisited):
                    return True 
            elif neighbour in pathvisited:
                return True
        pathvisited.remove(node)
        return False
    def isCyclic(self, V, adj):
        # code here
        visited = set()
        pathvisited = set()
        for i in range(V):
            if self.dfs(i,adj,visited,pathvisited):
                return 1 
        return 0
