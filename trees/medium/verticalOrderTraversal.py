import heapq

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [[root, 0, 0]]
        nodes_with_coordinates = []
        vertical_levels = {}

        while queue:
            node, x, y = queue.pop(0) 
            nodes_with_coordinates.append([node.val, x, y])

            if x in vertical_levels:
                heapq.heappush(vertical_levels[x], (y, node.val))
            else:
                vertical_levels[x] = [(y, node.val)]

            if node.left:
                queue.append([node.left, x - 1, y + 1])
            if node.right:
                queue.append([node.right, x + 1, y + 1])

        min_vertical_level = min(vertical_levels.keys())
        max_vertical_level = max(vertical_levels.keys())

        vertical_order = []

        for i in range(min_vertical_level, max_vertical_level + 1):
            if i in vertical_levels:
                temp = []
                while vertical_levels[i]:
                    temp.append(heapq.heappop(vertical_levels[i])[1])
                    print(temp)
                vertical_order.append(temp)
        print(nodes_with_coordinates)
        print(vertical_levels)
        return vertical_order
