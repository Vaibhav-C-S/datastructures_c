class UnionFind:
    def __init__(self,V):
        self.parent = [i for i in range(V)]
        self.size = [1] *V
    def find(self,node):
        if self.parent[node] ==  node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
    
class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        extraedges = 0
        for i,j in edges:
            if uf.find(i) != uf.find(j):
                uf.union(i,j)
            else:
                extraedges +=1 
        components = 0
        for i in range(n):
            if uf.parent[i] == i:
                components+=1
        
        ans = components - 1
        if extraedges >= ans : return ans 
        return -1
