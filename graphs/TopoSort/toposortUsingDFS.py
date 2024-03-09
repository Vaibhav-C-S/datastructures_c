class Solution:
    
    #Function to return list containing vertices in Topological order.
    def dfs(self,node,adj,visited,stack):
        visited.add(node)
        for neighbour in adj[node]:
            if neighbour not in visited:
                self.dfs(neighbour,adj,visited,stack)
        stack.append(node)
        
    def topoSort(self, V, adj):
        stack = []
        visited =set()
        for i in range(V):
            if i not in visited:
                self.dfs(i,adj,visited,stack)
        
        return stack[::-1]
