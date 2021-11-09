"""
We define a harmonious array as an array where the difference between its
maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest
harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some
or no elements without changing the order of the remaining elements.
"""

class Solution:
    def findLHS(self, nums) -> int:
        # counter = {}
        # for n in nums:
        #     if n not in counter:
        #         counter[n] = 0
        #     counter[n] += 1
        # max_seq = 0
        # # keys = sorted(list(counter.keys()))
        # # for i in range(len(keys)-1):
        # #     if keys[i+1]-keys[i] == 1:
        # #         if counter[keys[i]] + counter[keys[i+1]] > max_seq:
        # #             max_seq = counter[keys[i]] + counter[keys[i+1]]
        #
        # for k in counter.keys():
        #     if k+1 in counter:
        #         if counter[k] + counter[k+1] > max_seq:
        #             max_seq = counter[k] + counter[k+1]

        max_seq = 0
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

            if n-1 in counter:
                max_seq = max(max_seq, counter[n-1] + counter[n])
            if n+1 in counter:
                max_seq = max(max_seq, counter[n+1] + counter[n])

        return max_seq


sol = Solution()
nums = [1,3,2,2,5,2,3,7]
print(sol.findLHS(nums))

nums = [1,1,1,1,]
print(sol.findLHS(nums))
