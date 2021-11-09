"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if n == 0:
            return True
        p = 0
        l = len(flowerbed)
        while p < l:
            if flowerbed[p] == 0 and ((p-1 >= 0 and flowerbed[p-1] == 0) or p-1 == -1) and ((p + 1 < l and flowerbed[p+1] == 0) or p+1 == l):
                flowerbed[p] = 1
                n -= 1
                if n == 0:
                    return True
            p += 1
        return False



sol = Solution()
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(sol.canPlaceFlowers(flowerbed, n))

flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
print(sol.canPlaceFlowers(flowerbed, n))

flowerbed = [1, 0, 0, 0, 1]
n = 2
print(sol.canPlaceFlowers(flowerbed, n))

flowerbed = [0, 0, 1, 0, 1]
n = 1
print(sol.canPlaceFlowers(flowerbed, n))
