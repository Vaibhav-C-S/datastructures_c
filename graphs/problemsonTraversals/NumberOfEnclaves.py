class Solution:
    def dfs(self, grid, i, j, visited, m, n):
        visited[i][j] = True
        row_i = [-1, 0, 1, 0]
        col_j = [0, 1, 0, -1]
        for k in range(4): 
            new_i = i + row_i[k]
            new_j = j + col_j[k]
            if (0 <= new_i < m) and (0 <= new_j < n) and not visited[new_i][new_j] and grid[new_i][new_j] == 'O':
                self.dfs(grid, new_i, new_j, visited, m, n)

    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or j == n - 1 or i == m - 1) and grid[i][j] == 'O':
                    self.dfs(grid, i, j, visited, m, n)
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 'O':
                    grid[i][j] = 'X'
