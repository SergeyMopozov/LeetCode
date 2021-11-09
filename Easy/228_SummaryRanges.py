"""You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums):

        result = []
        start = 0
        end = 0

        if len(nums) == 0:
            return result

        for i in range(1, len(nums)):

            if nums[i] == nums[end] + 1:
                end = i
            elif end - start > 0:
                result.append(f"{nums[start]}->{nums[end]}")
                start = i
                end = i
            elif start == end:
                result.append(f"{nums[start]}")
                start = i
                end = i

        if end - start > 0:
            result.append(f"{nums[start]}->{nums[end]}")
        elif start == end:
            result.append(f"{nums[start]}")

        return result


sol = Solution()
n = [0, 1, 2, 4, 5, 7]      # Output: ["0->2","4->5","7"]
print(sol.summaryRanges(n))

n = [0, 1, 2]      # Output: ["0-2"]
print(sol.summaryRanges(n))

n = [0, 2]      # Output: ["0-2"]
print(sol.summaryRanges(n))

n = [0]      # Output: ["0"]
print(sol.summaryRanges(n))

n = []      # Output: []
print(sol.summaryRanges(n))
