"""
You are given a string s representing an attendance record for a student where each character signifies whether
the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.
"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = True
        late = True
        absent_count = 0
        curr_late = 0
        for c in s:
            if c == 'A':
                absent_count += 1
                if absent_count >= 2:
                    absent = False
                curr_late = 0
            elif c == 'L':
                curr_late += 1
                if curr_late == 3:
                    late = False
            elif c == 'P':
                curr_late = 0

        return absent and late


sol = Solution()
student = "PPALLP"
print(sol.checkRecord(student))

student = "PPALLL"
print(sol.checkRecord(student))