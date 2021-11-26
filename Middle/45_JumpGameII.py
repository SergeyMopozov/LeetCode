"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""


class Solution:
    def jump(self, nums) -> int:

        max_jump = 0
        jump_count = 0
        current = 0
        right_bound = 0
        while right_bound < len(nums) - 1:
            # find max between prev max_jump and sum from current possible jump to the next possible jump
            for idx in range(current, right_bound+1):
                max_jump = max(max_jump, idx+nums[idx])

            jump_count += 1

            # update current position and max_jump
            current = right_bound+1
            right_bound = max_jump

        return jump_count


sol = Solution()
nums = [2,3,1,1,4,0,1]
print(sol.jump(nums))

nums = [2,3,0,1,4]
print(sol.jump(nums))

nums = [2,3,1]
print(sol.jump(nums))

nums = [3,4,3,2,5,4,3]
print(sol.jump(nums))

nums = [1,1,1,1]
print(sol.jump(nums))

nums = [1,2,1,1,1]
print(sol.jump(nums))

nums = [10,9,8,7,6,5,4,3,2,1,1,0]
print(sol.jump(nums))