"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""

class Solution:
    def permute(self, nums):

        def _perm(nums):
            # pool of combinations
            pool = tuple(nums)
            # len of combinations
            n = len(pool)

            indices = list(range(n))
            cycles = list(range(n, 0, -1))

            yield tuple(pool[i] for i in indices[:n])

            while n:
                for i in reversed(range(n)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i + 1:] + indices[i:i + 1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:n])
                        break
                else:
                    return

        return [list(p) for p in _perm(nums)]

sol = Solution()
nums = [1, 2, 3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permute(nums))
