class Solution:
    def convertintoadjList(self,mat,V):
        adjL = [ [] for _ in range(V)] 
        for i in range(V):
            for j in range(V):
                if mat[i][j] == 1 and i!=j:
                    adjL[i].append(j)
                    adjL[j].append(i)
        
        return adjL

    def dfs(self,node,visited,adj):
        visited.add(node)
        for neighbour in adj[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                self.dfs(neighbour,visited,adj)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = self.convertintoadjList(isConnected,len(isConnected))
        count = 0
        V = len(isConnected)
        visited = set()
        
        for i in range(V):
            if i not in visited:
                visited.add(i)
                self.dfs(i,visited,adj)
                count+=1
        return count

        
