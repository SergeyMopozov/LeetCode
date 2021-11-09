"""
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    string = str(x)
    # check that symbols is digits
    if not set(string).issubset(set([str(n) for n in range(0, 10)])):
        return False
    else:
        start = 0
        end = len(string) - 1
        for i in range(len(string) // 2):
            if string[start + i] != string[end - i]:
                return False
        return True


x = 12321
isPalindrome(x)
