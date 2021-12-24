"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def _dsp(node, depths, counter):
            if node:
                counter += 1
                if node.children:
                    for c in node.children:
                        _dsp(c, depths, counter)
                else:
                    _dsp(node.children, depths, counter)
            else:
                depths.append(counter)


        depths = []
        _dsp(root, depths, 0)

        return max(depths)
