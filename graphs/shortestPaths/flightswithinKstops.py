from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i,j,w in flights:
            if i not in adj:
                adj[i] = [(j,w)]
            else:
                adj[i].append((j,w))
        queue= deque()
        queue.append((0,0,src))
        distance = [(float("inf"))]*n 
        while queue:
            stops,dis,node = queue.popleft()
            for neighbour,w in adj.get(node,[]):
                    if dis +  w < distance[neighbour] and stops <= k :
                        distance[neighbour] = dis +  w
                        queue.append((stops+1,dis+w,neighbour))
        print(distance)
        if distance[dst] == float("inf"):
            return -1
        return distance[dst]

        
