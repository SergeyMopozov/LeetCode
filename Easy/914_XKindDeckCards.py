"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1
or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
"""

class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        import collections
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N + 1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False




sol = Solution()
deck = [1,2,3,4,4,3,2,1]
print(sol.hasGroupsSizeX(deck))

deck = [1,1,1,2,2,2,3,3]
print(sol.hasGroupsSizeX(deck))

deck = [1]
print(sol.hasGroupsSizeX(deck))

deck = [1,1,2,2,2,2]
print(sol.hasGroupsSizeX(deck))
