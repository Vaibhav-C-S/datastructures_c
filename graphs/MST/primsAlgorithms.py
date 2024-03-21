#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap,(0,0,-1))
        visited = set()
        parents={}
        total_weight = 0
        while heap:
            weight,node,parent = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if parent != -1:
                parents[parent] = node
            total_weight+=weight
            for neighbour,w in adj[node]:
                if neighbour not in visited:
                    heapq.heappush(heap,(w,neighbour,node))
        print(parents)
        return total_weight
