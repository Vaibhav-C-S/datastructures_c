class UnionFind:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.size = [1] * V

    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        u_parent = self.find_parent(u)
        v_parent = self.find_parent(v)
        if self.size[u_parent] < self.size[v_parent]:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]
        else:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]

class Solution:
    
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        uf = UnionFind(V)
        edges = []
        for i in range(V):
            for j, w in adj[i]:
                edges.append([i, j, w])
        edges.sort(key=lambda x: x[2])
        total = 0
        for u, v, w in edges:
            if uf.find_parent(u) != uf.find_parent(v):
                uf.union_by_size(u, v)
                print(u,v)
                total += w
        return total
