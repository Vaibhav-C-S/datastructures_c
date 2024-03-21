class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float(inf) for _ in range(n)] for _ in range(n)]
        for i,j,w in edges:
            matrix[i][j] = w
            matrix[j][i] = w
        for i in range(n):
            matrix[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j],matrix[i][k] + matrix[k][j])
        mini = float("inf")
        citynum = 0
        print(matrix)
        for i in range(n):
            count = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold:
                    count+=1
            if count <= mini:
                mini = count
                citynum = i
        return citynum


