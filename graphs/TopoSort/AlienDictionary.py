def findOrder(self,words, N, K):
    # code here
        graph = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
    
        stack = []
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            stack.append(node)
        for c in graph:
            if c not in visited:
                dfs(c)
        
        if len(stack) == len(graph):
            return "".join(stack[::-1])
        return ""
