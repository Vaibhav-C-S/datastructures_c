import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n = len(heights)
        m = len(heights[0])
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0, 0))
        distance = [[float("inf") for _ in range(m)] for _ in range(n)]
        row_i = [-1, 0, 1, 0]
        col_j = [0, 1, 0, -1]
        distance[0][0] = 0
        while heap:
            diff, curr_i, curr_j = heapq.heappop(heap)
            if curr_i == n-1 and curr_j == m-1:return distance[n-1][m-1]
            for i in range(4):
                new_i = row_i[i] + curr_i
                new_j = col_j[i] + curr_j
                if 0 <= new_i < n and 0 <= new_j < m:
                    new_diff = max(diff, abs(heights[curr_i][curr_j] - heights[new_i][new_j]))
                    if new_diff < distance[new_i][new_j]:
                        heapq.heappush(heap, (new_diff, new_i, new_j))
                        distance[new_i][new_j] = new_diff
        return 0
