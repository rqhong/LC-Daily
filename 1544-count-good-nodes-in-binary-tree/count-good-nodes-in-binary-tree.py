# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global count_gn  # 宣告 count_gn 為全域變數
        count_gn = 0

        def findGoodNodes(node, max_p_v):
            global count_gn
            if node.val >= max_p_v:
                count_gn += 1
                max_p_v = node.val
            if node.left:
                findGoodNodes(node.left, max_p_v)
            if node.right:
                findGoodNodes(node.right, max_p_v)
        findGoodNodes(root, root.val)

        return count_gn