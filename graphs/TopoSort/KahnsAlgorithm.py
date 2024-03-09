from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    
        
    def topoSort(self, V, adj):
        indegree=[0]* V
        for node in range(V):
            for neighbour in adj[node]:
                indegree[neighbour]+=1
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        return ans
                
            
