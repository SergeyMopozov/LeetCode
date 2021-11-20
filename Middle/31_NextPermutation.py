"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange
it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""


def swap(n, i, j):
    n[i], n[j] = n[j], n[i]


def reverse(n, start):
    end = len(n) - 1
    while start < end:
        swap(n, start, end)
        start += 1
        end -= 1


def permutation(nums):
    pointer1 = len(nums) - 2
    while pointer1 >= 0 and nums[pointer1 + 1] <= nums[pointer1]:
        pointer1 -= 1

    if pointer1 >= 0:
        pointer2 = len(nums) - 1
        while nums[pointer2] <= nums[pointer1]:
            pointer2 -= 1

        swap(nums, pointer1, pointer2)
    reverse(nums, pointer1 + 1)


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        permutation(nums)


# def next_permutation(A) -> None:
#
#     if not A:
#         raise ValueError(f'given array A is empty list')
#
#     # step 1
#     g = idx_of_digit_larger_than_left_adj_digit(A)
#
#     if g is not None:
#         # step 2
#         p = idx_of_farthest_digit_larger_than(g - 1, A)
#         swap(A, g - 1, p)
#
#         reverse_from = g
#     else:
#         reverse_from = 0
#
#     # step 3
#     reverse_in_place(A, reverse_from)
#
#
# def idx_of_digit_larger_than_left_adj_digit(A):
#     i = len(A) - 1
#
#     while i > 0:
#         if A[i - 1] < A[i]:
#             return i
#         i -= 1
#
#
# def idx_of_farthest_digit_larger_than(idx: int, A) -> int:
#     e = A[idx]
#
#     for k in range(idx + 1, len(A)):
#         if A[k] <= e:
#             return k - 1  # returning index of previous digit
#     else:
#         return len(A) - 1
#
#
# def reverse_in_place(A, i: int) -> None:
#     """
#     reversing sub array A[i:] in place
#     :param A:
#     :param i:
#     """
#     j = len(A) - 1
#
#     while i < j:
#         swap(A, i, j)
#         i += 1
#         j -= 1
#
#
# def swap(A, i: int, j: int) -> None:
#     A[i], A[j] = A[j], A[i]
#
#
# class Solution:
#     def nextPermutation(self, A) -> None:
#         next_permutation(A)


sol = Solution()

nums = [1,2,3]
print(nums)
sol.nextPermutation(nums)
print(nums)



