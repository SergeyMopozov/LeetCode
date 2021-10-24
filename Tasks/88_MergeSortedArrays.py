"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # res = []
        # f = 0
        # s = 0
        # nums2.insert()
        # while f < m or s < n:
        #
        #     if f == m and s < n:
        #         for i in nums2[s:]:
        #             res.append(nums2[s])
        #             s += 1
        #     elif s == n and f < m:
        #         res.append(nums1[f])
        #         f += 1
        #     else:
        #         if nums1[f] < nums2[s]:
        #             res.append(nums1[f])
        #             f += 1
        #         else:
        #             res.append(nums2[s])
        #             s += 1

        s = 0

        for f in range(m):
            if nums2[s] < nums1[f]:
                for i, x in enumerate(nums1[f:m], f):
                    nums1[i+1] = x
                nums1[f] = nums2[s]
                s += 1
        if m < n:
            for i, x in enumerate(nums2[s:], f+s+1):
                nums1[i] = x


sol = Solution()
a = [1, 2, 3, 0, 0, 0, 0, 0]
b = [2, 4, 5, 6, 7]

# print(sol.merge(a, len(a), b, len(b)))
print(a)
sol.merge(a, len(a) - len(b), b, len(b))
print(a)
