"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums) -> bool:
        # if len(nums) == 1:
        #     return True
        # curr = 0            # current position
        # jumps = nums[curr]  # available jumps
        # bound = 0
        # max_jump = 0
        # while jumps != 0:                       # while available jumps - jump
        #     for i in range(curr, bound+1):      # find maximum available jumps
        #         if i < len(nums):
        #             jumps = max(jumps, i + nums[i])
        #
        #     curr = bound + 1                       # jump!
        #     bound = jumps
        #
        #     print(curr, jumps)
        #     if max_jump >= len(nums) - 1:            # if jump out return True
        #         return True
        #     else:
        #         jumps = nums[curr]              # set available jumps in current positon
        #     print(curr, jumps)
        # return False

        req = 0
        for i in range(len(nums)-1, -1, -1):
            #print(i)
            if nums[i] >= req:
                req = 0
            req += 1

        if req > 1:
            return False
        else:
            return True


sol = Solution()
nums = [2,3,1,1,4]
print(sol.canJump(nums))

nums = [3, 2, 1, 0, 4]
print(sol.canJump(nums))

nums = [0]
print(sol.canJump(nums))

nums = [2, 0]
print(sol.canJump(nums))

nums = [2, 0, 0]
print(sol.canJump(nums))

nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print(sol.canJump(nums))
