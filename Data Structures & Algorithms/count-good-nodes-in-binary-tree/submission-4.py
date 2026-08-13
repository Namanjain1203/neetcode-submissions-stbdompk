# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root):
        def dfs(node,till_now_max):
            if not node:
                return 0
            good = 1 if node.val >= till_now_max else 0
            new_max = max(till_now_max,node.val)
            left = dfs(node.left,new_max)
            right = dfs(node.right,new_max)
            return good + left + right
        return dfs(root,float('-inf'))