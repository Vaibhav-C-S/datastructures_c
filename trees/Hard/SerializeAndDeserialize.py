# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialize = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is None:
                serialize.append("N")  
                continue
            serialize.append(str(node.val))
            if node.left:
                queue.append(node.left)
            else:
                queue.append(None)
            if node.right:
                queue.append(node.right)
            else:
                queue.append(None)
        print(serialize)
        return ",".join(serialize)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'N':
            return None  
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if data[index] != "N":
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1
            if data[index] != "N":
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1
        return root
                



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
