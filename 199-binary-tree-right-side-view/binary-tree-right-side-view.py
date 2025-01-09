# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        queue = defaultdict(list)

        queue[0].append(root)
        res = []
        i = 1

        while queue[i-1]:

            node = queue[i-1].pop(0)
           
            if node.left:
                queue[i].append(node.left)
            if node.right:
                queue[i].append(node.right)
            if not queue[i-1]:
                res.append(node.val)
                i += 1
        return res

            
            