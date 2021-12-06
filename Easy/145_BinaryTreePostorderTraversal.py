"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):

        result = []
        if not root:
            return result

        stack = []
        node = root

        while node or len(stack) != 0:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result
