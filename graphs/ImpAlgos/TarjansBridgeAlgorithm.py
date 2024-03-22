def findBridges(edges, v, e):
    timer = 1
    adj = {i: [] for i in range(v)}
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    time = [0] * v
    low = [0] * v
    ans = []
    visited = set()

    # Write your code here
    def dfs(node, visited, time, low, ans, adj, parent):
        nonlocal timer
        visited.add(node)
        low[node] = timer
        time[node] = timer
        timer += 1
        for neighbour in adj[node]:
            if neighbour == parent:
                continue
            if neighbour not in visited:
                dfs(neighbour, visited, time, low, ans, adj, node)
                low[node] = min(low[node], low[neighbour])
                if low[neighbour] > time[node]:
                    ans.append([node, neighbour])
            else:
                low[node] = min(low[node], low[neighbour])

    dfs(0, visited, time, low, ans, adj, -1)
    return ans
