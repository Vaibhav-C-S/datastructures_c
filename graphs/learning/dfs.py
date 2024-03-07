#User function Template for python3
#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        dfs = []
        def helper(node,visited,dfs):
            visited.add(node)
            dfs.append(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    helper(neighbour,visited,dfs)
        visited = set()
        
        helper(0,visited,dfs)
        return dfs

--------------------
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        dfs = []
        adjMatrix = [[0]* V for _ in range(V)]
        for i in range(V):
            for j in adj[i]:
                adjMatrix[i][j] = 1
        
        def helper(node,V,visited,dfs,adj):
            visited.add(node)
            dfs.append(node)
            for neighbour in range(V):
                if adj[node][neighbour] == 1 and neighbour not in visited:
                    helper(neighbour,V,visited,dfs,adj)
        visited = set()
        
        helper(0,V,visited,dfs,adjMatrix)
        return dfs
