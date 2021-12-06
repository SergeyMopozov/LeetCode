"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []
        if not root:
            return result
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return result
