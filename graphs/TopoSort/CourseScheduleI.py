from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        V = numCourses
        adj =[[] for _ in range(V) ]
        for pre,course in prerequisites:
            adj[pre].append(course)
        indegree = [0]*V
        queue= deque()
        for i in range(V):
            for neighbour in adj[i]:
                indegree[neighbour]+=1
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        completed = 0
        while queue:
            node = queue.popleft()
            completed+=1
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        if completed==V:
            return True
        return False

            
        
