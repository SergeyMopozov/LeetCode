"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count_st = {}
        for s in stones:
            if s not in count_st:
                count_st[s] = 0
            count_st[s] += 1

        result = 0
        for j in jewels:
            if j in count_st:
                result += count_st[j]

        return result

sol = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(sol.numJewelsInStones(jewels, stones))
