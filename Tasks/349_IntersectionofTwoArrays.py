"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

II
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times
as it shows in both arrays and you may return the result in any order.


"""

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))

    def fullIntersection(self, nums1, nums2):
        dn_1 = {}
        dn_2 = {}

        for n in nums1:
            if n not in dn_1:
                dn_1[n] = 0
            dn_1[n] += 1

        for n in nums2:
            if n not in dn_2:
                dn_2[n] = 0
            dn_2[n] += 1

        result = []
        for k in dn_1:
            if k in dn_2:
                for i in range(min(dn_1[k], dn_2[k])):
                    result.append(k)

        return result




sol = Solution()
n1 = [4, 9, 9, 5]
n2 = [9, 4, 9, 8, 4]
print(sol.intersection(n1, n2))
print(sol.fullIntersection(n1, n2))
