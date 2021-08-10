## leet code task 1 10/06/2020

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # from itertools import combinations
        # pairs = {p[0]+p[1]:p for p in combinations(nums, 2)}
        # for duble number return first founded
        # idx =  [nums.index(p) for p in pairs.get(target, 'Not found')]
        # return idx

        # # 2. iterate over array for find sum
        # for idx, first_value in enumerate(nums):
        #     for jdx, second_value in enumerate(nums[idx + 1:]):
        #         if (first_value + second_value) == target:
        #             return [idx, idx + 1 + jdx]
        # return [None, None]

        # use dictionary
        dict_nums = {}
        for idx, n in enumerate(nums):
            complement = target - nums[idx]
            if complement in dict_nums.keys():
                return [dict_nums.get(complement), idx]
            dict_nums[nums[idx]] = idx





s = Solution()
s.twoSum([2, 7, 11, 15], 9)