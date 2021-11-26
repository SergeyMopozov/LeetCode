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

        other = nums1[:m]
        p1 = p2 = 0
        for k in range(len(nums1)):
            if p1 < n and (p2 == m or nums2[p1] < other[p2]):
                nums1[k] = nums2[p1]
                p1 += 1
            else:
                nums1[k] = other[p2]
                p2 += 1


sol = Solution()
a = [1, 2, 3, 0, 0, 0, 0, 0]
b = [2, 4, 5, 6, 7]

# print(sol.merge(a, len(a), b, len(b)))
print(a)
sol.merge(a, len(a) - len(b), b, len(b))
print(a)

a = [1]
b = []

# print(sol.merge(a, len(a), b, len(b)))
print(a)
sol.merge(a, len(a) - len(b), b, len(b))
print(a)
