#User function template for Python time o(n3) and space o(n2)

class Solution:
	def shortest_distance(self, matrix):
		#Code here
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float("inf")
        for k in range(n):
         for i in range(n):
             for j in range(n):
                 matrix[i][j] = min(matrix[i][j],matrix[i][k]+ matrix[k][j])
        
        for i in range(n):
         for j in range(n):
             if matrix[i][j] == float("inf"):
                 matrix[i][j] = -1 
		 
#         #checking negative cycle
#         for i in range(n):
#             for j in range(n):
#                 if (i==j) and matrix[i][j]<0:
#                     return "has negative cycle"
# #{ 
