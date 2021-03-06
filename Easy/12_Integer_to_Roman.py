"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Constrains:
1 <= num <= 3999
"""


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    base_num = {1: 'I', 4: 'IV',
                5: 'V', 9: 'IX', 10: 'X', 40:'XL',  50: 'L', 90:'XC', 100: 'C', 400:'CD',  500: 'D', 900: 'CM', 1000: 'M'}

    convert_str = ''
    for k in sorted(base_num.keys(), reverse=True):
        quotient = num // k

        if quotient !=0:
            for _ in range(quotient):
                convert_str += base_num[k]
            rest = num % k
            num = rest

    return convert_str

print(intToRoman(1994))
