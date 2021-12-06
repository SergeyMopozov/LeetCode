"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


"""


class Solution:
    def insert(self, intervals, newInterval):
        def merge(intervals):
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
        intervals.append(newInterval)
        return merge(intervals)


sol = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(sol.insert(intervals, newInterval))
