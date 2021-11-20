"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which,
together with the x-axis forms a container, such that the container contains the most water.
"""

import itertools

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # brut force
    # area = 0
    # for i, left in enumerate(height):
    #     for j, right in enumerate(height[1:], 1):
    #         length = j-i
    #         if min(left, right) * length > area:
    #             area = min(left, right) * length

    left = 0
    right = len(height) - 1
    area = 0
    while left < right:
        area = max(area, min(height[left],height[right])*(right-left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return area


print(maxArea([1, 2, 3]))



