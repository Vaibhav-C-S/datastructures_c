class Solution:
    #Function to detect cycle in an undirected graph.
    def bfs(self,node,adj,visited):
        queue = deque()
        queue.append((node,None))
        visited.add(node)
        while queue:
            node,parent = queue.popleft()
            for neighbour in adj[node]:
                if neighbour not in visited:
                    queue.append((neighbour,node))
                    visited.add(neighbour)
                elif neighbour != parent:
                    return True
        return False
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		V = len(adj)
		visited = set()
		for i in range(V):
		    if i not in visited:
		        if self.bfs(i,adj,visited) == True:
		            return 1 
		return 0
