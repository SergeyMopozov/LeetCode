"""

"""


class Solution:
    def findMiddleIndex(self, nums) -> int:

        if len(nums) == 1:
            return 0

        prefix = [nums[0]]
        for n in nums[1:]:
            prefix.append(prefix[-1] + n)
        leftmost = -1
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if prefix[i - 1] == 0:
                    leftmost = i
                    break
            elif i == 0:
                if 0 == prefix[-1] - prefix[i - 1] - nums[i]:
                    leftmost = i
                    break
            elif i != 0 and i != len(nums) - 1:
                if prefix[i - 1] == prefix[-1] - prefix[i - 1] - nums[i]:
                    leftmost = i
                    break

        return leftmost

        # for i in range(len(nums)):
        #     leftsum = sum(nums[:i])
        #     rightsum = sum(nums[i + 1:])
        #
        #     if leftsum == rightsum:
        #         return i
        #
        # return -1

sol = Solution()
nums = [1,1,1,1]
print(sol.findMiddleIndex(nums))

nums = [0, 0, 0, 0]
print(sol.findMiddleIndex(nums))
