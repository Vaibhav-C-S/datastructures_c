from collections import deque

class Solution:
    def minimum_multiplications(self, arr, start, end):
        q = deque([(start, 0)])
        dist = [float('inf')] * 100000
        dist[start] = 0
        mod = 100000

        while q:
            node, steps = q.popleft()

            for it in arr:
                num = (it * node) % mod

                if steps + 1 < dist[num]:
                    dist[num] = steps + 1
                    if num == end:
                        return steps + 1
                    q.append((num, steps + 1))

        return -1
