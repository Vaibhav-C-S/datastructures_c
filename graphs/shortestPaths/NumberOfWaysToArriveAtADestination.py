import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Creating an adjacency list for the given graph.
        adj = {}
        for i, j, w in roads:
            if i not in adj:
                adj[i] = [(j, w)]
            else:
                adj[i].append((j, w))
            if j not in adj:
                adj[j] = [(i, w)]
            else:
                adj[j].append((i, w))

        ways = [0] * n 
        ways[0] = 1
        distance = [float("inf")] * n
        distance[0] = 0
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap,(0,0))
        while heap:
            dis, node = heapq.heappop(heap)
            for neighbour, w in adj.get(node, []):
                if dis + w < distance[neighbour]:
                    distance[neighbour] = dis + w
                    heapq.heappush(heap, (dis+w, neighbour))
                    ways[neighbour] = ways[node]
                elif dis + w == distance[neighbour]:
                    ways[neighbour] += ways[node]
        return ways[n-1] % (10**9 + 7)
