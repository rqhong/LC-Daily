# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = defaultdict(list)
        res = defaultdict(list)
        level = 0
        queue[0].append(root)
        res[0].append(root.val)

        while queue[level]:
            node = queue[level].pop()
            if node.left:
                queue[level+1].append(node.left)
                res[level+1].append(node.left.val)
            if node.right:
                queue[level+1].append(node.right)
                res[level+1].append(node.right.val)
            if not queue[level]:
                level += 1
        del queue
        m = float("-inf")
        for k, v in res.items():
            m = max(m, sum(v))
        for k in res.keys():
            if sum(res[k]) == m:
                return k+1
        return None