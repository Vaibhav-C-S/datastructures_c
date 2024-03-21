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
