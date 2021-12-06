"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of
the non-overlapping intervals that cover all the intervals in the input.
"""
class Solution:
    def merge(self, intervals):
        result = []
        intervals = sorted(intervals, key=lambda x: x[0])
        curr = intervals[0]
        for pair in intervals[1:]:
            if pair[0] <= curr[1] <= pair[1]:
                curr[1] = pair[1]
            elif pair[1] <= curr[1]:
                pass
            else:
                result.append(curr)
                curr = pair

        result.append(curr)

        return result


sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
print(sol.merge(intervals))

intervals = [[1,4],[4,5]]
print(sol.merge(intervals))

intervals = [[1,3]]
print(sol.merge(intervals))

intervals = [[1,4],[2,3]]
print(sol.merge(intervals))

