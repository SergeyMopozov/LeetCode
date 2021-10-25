"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        while columnNumber != 0 :
            #print(columnNumber, columnNumber % 26)
            rest = columnNumber % 26
            result.append(symbols[rest - 1])
            columnNumber = columnNumber // 26
            if rest == 0:
                columnNumber = columnNumber - 1
        return ''.join(result[::-1])

    def titleToNumber(self, columnTitle: str) -> int:
        symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = 0
        for i, c in enumerate(columnTitle[::-1], 0):
            number += (symbols.index(c) + 1) * 26**i
        return number

sol = Solution()
# n = 701 #ZY
# print(sol.convertToTitle(n))
#
# n = 2147483647 #FXSHRXW
# print(sol.convertToTitle(n))
#
# n = 52 #AZ
# print(sol.convertToTitle(n))
#
# n = 26 #Z
# print(sol.convertToTitle(n))
#
# n = 28 #AB
# print(sol.convertToTitle(n))

s = 'AB' #28
print(sol.titleToNumber(s))

s = 'FXSHRXW' #2147483647
print(sol.titleToNumber(s))
