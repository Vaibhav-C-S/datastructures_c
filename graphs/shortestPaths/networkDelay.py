import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        adj = {}
        for i,j,w in times:
            if i not in adj:
                adj[i] = [(j,w)]
            else:
                adj[i].append((j,w))
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap,(0,src))
        distance = [float("inf")]*(n+1)
        distance[src] = 0
        while heap:
            dis,node = heapq.heappop(heap)
            for neighbour,w in adj.get(node,[]):
                if distance[node] + w < distance[neighbour]:
                    distance[neighbour] = distance[node] + w
                    heapq.heappush(heap,(distance[neighbour],neighbour))
        distance.pop(0)
        for i in range(len(distance)):
            if distance[i] == float("inf") :return -1
        return max(distance)
        
