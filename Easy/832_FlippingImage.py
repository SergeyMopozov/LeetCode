"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
"""

class Solution:
    def flipAndInvertImage(self, image):
        rows = len(image)
        cols = len(image[0])
        for i in range(rows):
            left = 0
            right = cols - 1
            while left < right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                left += 1
                right -= 1
            for j in range(cols):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        return image


sol = Solution()
image = [[1,1,0],[1,0,1],[0,0,0]]
#Output: [[1,0,0],[0,1,0],[1,1,1]]
print(sol.flipAndInvertImage(image))
