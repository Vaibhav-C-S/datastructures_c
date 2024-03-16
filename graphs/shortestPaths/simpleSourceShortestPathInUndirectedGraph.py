#all the weights are considered to be unit,solved in coding ningjas
from typing import List
from collections import deque
def shortestPath(n:int, edges: List[List[int]], src:int ) -> List[int]:
    # Write your code here
    adj = [[]for _ in range(n)]
    for i,j in edges:
        adj[i].append(j)
        adj[j].append(i)
    queue = deque()
    queue.append((src,0))
    visited = set()
    visited.add(src)
    distance = [float("inf")]*n
    distance[src] = 0
    while queue:
        node,dist = queue.popleft()
        for neighbour in adj[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                distance[neighbour] = min(distance[neighbour],dist+1)
                queue.append((neighbour,dist+1))
    for i in range(n):
        if distance[i] == float("inf"):
            distance[i] = -1 
    return distance
