"""
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there
is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""


class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        # def _isntNearest(arr, value, diff):
        #     # binary search
        #
        #     left = 0
        #     right = len(arr) - 1
        #
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if abs(value - arr[mid]) <= diff:
        #             return False
        #         if abs(value - arr[mid]) > diff:
        #             left = mid+1
        #         else:
        #             right = mid - 1
        #     return True

        def get_nearest(arr, value):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > value:
                    right = mid - 1
                else:
                    left = mid + 1
            return left, right

        arr2 = sorted(arr2)
        counter = 0
        for n in arr1:
            l, r = get_nearest(arr2, n)
            if abs(n-l) > d and abs(n-r) > d:
                counter += 1
        return counter



sol = Solution()
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(sol.findTheDistanceValue(arr1, arr2, d))


arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
print(sol.findTheDistanceValue(arr1, arr2, d))

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6
print(sol.findTheDistanceValue(arr1, arr2, d))

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
print(sol.findTheDistanceValue(arr1, arr2, d))

arr1 = [-3,10,2,8,0,10]
arr2 = [-9,-1,-4,-9,-8]
d = 9
print(sol.findTheDistanceValue(arr1, arr2, d))


arr1 = [-803,715,-224,909,121,-296,872,807,715,407,94,-8,572,90,-520,-867,485,-918,-827,-728,-653,-659,865,102,-564,-452,554,-320,229,36,722,-478,-247,-307,-304,-767,-404,-519,776,933,236,596,954,464]
arr2 = [817,1,-723,187,128,577,-787,-344,-920,-168,-851,-222,773,614,-699,696,-744,-302,-766,259,203,601,896,-226,-844,168,126,-542,159,-833,950,-454,-253,824,-395,155,94,894,-766,-63,836,-433,-780,611,-907,695,-395,-975,256,373,-971,-813,-154,-765,691,812,617,-919,-616,-510,608,201,-138,-669,-764,-77,-658,394,-506,-675,523,730,-790,-109,865,975,-226,651,987,111,862,675,-398,126,-482,457,-24,-356,-795,-575,335,-350,-919,-945,-979,611]
d = 37
print(sol.findTheDistanceValue(arr1, arr2, d))
