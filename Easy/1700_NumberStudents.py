"""

"""

from collections import deque


class Solution:
    def countStudents(self, students, sandwiches) -> int:

        students = deque(students)

        while sandwiches and len(set(students).intersection(set([sandwiches[0]]))) != 0:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.popleft()
                # eat += 1
            else:
                st = students.popleft()
                students.append(st)

        return len(students)


sol = Solution()
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(sol.countStudents(students, sandwiches))
#
#
# students = [0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1]
# sandwiches = [1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0]
# print(sol.countStudents(students, sandwiches))

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(sol.countStudents(students, sandwiches))
