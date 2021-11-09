"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""


class Solution:
    def fourSum(self, nums, target):
        # #1 brute force n^4 complexity
        # results = {}
        # n = len(nums)
        # for i in range(n - 3):
        #     for j in range(i+1, n-2):
        #         for k in range(j + 1, n - 1):
        #             for l in range(k + 1, n):
        #                 if nums[i] + nums[j] + nums[k] + nums[l] == target:
        #                     if tuple(sorted([nums[i], nums[j], nums[k], nums[l]])) not in results:
        #                         results[tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))] = [nums[i], nums[j],
        #                                                                                         nums[k], nums[l]]
        #
        # return list(results.values())

        # #2 n^3 complexity
        results = {}
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 3):
            for j in range(i+1, n-2):
                k = j+1
                l = n-1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        if tuple(sorted([nums[i], nums[j], nums[k], nums[l]])) not in results:
                            results[tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))] = [nums[i], nums[j],
                                                                                            nums[k], nums[l]]
                        k += 1
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1

        return list(results.values())


n1 = [1, 0, -1, 0, -2, 2]
t1 = 0

# Expected Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

n2 = [2, 2, 2, 2, 2]
t2 = 8
s = Solution()
print(s.fourSum(n1, t1))
print(s.fourSum(n2, t2))

