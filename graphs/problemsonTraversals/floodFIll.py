from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        row_i = [-1,0,1,0]
        col_j = [0,1,0,-1]
        queue = deque()
        queue.append((sr,sc))
        node_color = image[sr][sc]
        image[sr][sc] = color
        if node_color == color:
            return image
        while queue:
            curr_i,curr_j = queue.popleft()
            for i in range(4):
                new_i = curr_i + row_i[i]
                new_j = curr_j + col_j[i]
                if (0<=new_i<m) and (0<=new_j<n) and image[new_i][new_j] == node_color:
                    image[new_i][new_j] = color
                    queue.append((new_i,new_j))
        
        
        return image
