class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        V = numCourses
        adj =[[] for _ in range(V) ]
        for pre,course in prerequisites:
            adj[course].append(pre)
        indegree = [0]*V
        queue= deque()
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
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        if len(ans)==V: return ans
        return []
        
    
        

            
        
        
