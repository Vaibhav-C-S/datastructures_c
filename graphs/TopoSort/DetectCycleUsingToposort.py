#User function Template for python3
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    
      
    def isCyclic(self, V, adj):
        # code here\
        queue = deque()
        
        indegree = [0]*V;
        for i in range(V):
            for neighbour in adj[i]:
                indegree[neighbour]+=1
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        if len(ans) == V:
            return 0
        return 1
        
