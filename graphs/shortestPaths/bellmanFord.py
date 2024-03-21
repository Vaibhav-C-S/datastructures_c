class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    # o(v * e) time complexity
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        distance = [float("inf")]*V
        distance[S] = 0
        for _ in range(V-1):
            for i,j,w in edges:
                if distance[i]+ w < distance[j]:
                    distance[j] = distance[i]+ w
        for i,j,w in edges:
                if distance[i]+ w < distance[j]:
                    return [-1]
        for i in range(V):
            if distance[i] == float("inf"):
                distance[i] = 100000000

        return distance

