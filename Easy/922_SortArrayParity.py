"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.
"""


class Solution:
    def sortArrayByParityII(self, nums):

        # for i in range(len(nums)//2):
        #     if i % 2 == 1:
        #         nums[i], nums[i+len(nums)//2-1] = nums[i+len(nums)//2-1], nums[i]
        #
        # return nums

        # for i in range(len(nums)):
        #     if i % 2 == 0 and nums[i] % 2 != 0:
        #         # find even
        #
        #         for j in range(i+1, len(nums)):
        #             if j % 2 != 0 and nums[j] % 2 == 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        #     elif i % 2 != 0 and nums[i] % 2 == 0:
        #
        #         # find odd
        #         for j in range(i+1, len(nums)):
        #             if j % 2 == 0 and nums[j] % 2 != 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        # return nums

        even = 0
        odd = 1

        while even <= len(nums)-2 and odd <= len(nums)-1:
            if nums[even] % 2 != 0:
                if nums[odd] % 2 == 0:
                    nums[even], nums[odd] = nums[odd], nums[even]
                    even += 2
                else:
                    odd += 2
            else:
                even += 2
            if nums[odd] % 2 == 0:
                if nums[even] % 2 != 0:
                    nums[even], nums[odd] = nums[odd], nums[even]
                else:
                    even += 2
            else:
                odd += 2
        return nums




sol = Solution()
nums = [4,2,5,7]
print(sol.sortArrayByParityII(nums))

nums = [2, 3]
print(sol.sortArrayByParityII(nums))

nums = [3, 4]
print(sol.sortArrayByParityII(nums))

nums = [1,2,3,3,2,3,0,4]
print(sol.sortArrayByParityII(nums))


