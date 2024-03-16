from  typing import *
from collections import deque
def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    adj = {}
    for i,j,w in edges:
        if i not in adj:
            adj[i] = [(j,w)]
        else:
            adj[i].append((j,w))
    stack = deque()
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbour,weight in adj.get(node,[]):
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(node)
    for i in range(n):
        if i not in visited:
            dfs(i)
    distance = [float("inf")]*n
    distance[0] = 0 
    while stack:
        node = stack.pop()
        for neighbour,weight in adj.get(node,[]):
                if distance[node] + weight < distance[neighbour]:
                    distance[neighbour]=distance[node]+ weight
    
    for i in range(n):
        if distance[i] == float("inf"):
            distance[i] = -1 
    return distance
