"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self, nums):
        # output = [[]]
        #
        # for num in nums:
        #     #print(output)
        #     output += [curr + [num] for curr in output]
        #
        # return output

        # n = len(nums)
        # output = []
        #
        # for i in range(2 ** n, 2 ** (n + 1)):
        #     # generate bitmask, from 0..00 to 1..11
        #     bitmask = bin(i)[3:]
        #     print(i, bin(i), bitmask)
        #     # append subset corresponding to that bitmask
        #     print([nums[j] for j in range(n) if bitmask[j] == '1'])
        #     output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        #
        # return output

        def backtrack(first, curr):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0, [])
        return output


sol = Solution()
nums = [1, 2, 3]
print(sol.subsets(nums))
