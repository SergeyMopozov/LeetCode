"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you,
and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either
a $5, $10, or $20 bill. You must provide the correct change to each customer
so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays,
return true if you can provide every customer with correct change, or false otherwise.
"""

class Solution:
    def lemonadeChange(self, bills) -> bool:

        change_dict = {}

        for b in bills:
            if b not in change_dict:
                change_dict[b] = 0
            change_dict[b] += 1

            if b == 10:
                if 5 in change_dict and change_dict[5] >= 1:
                    change_dict[5] -= 1
                else:
                    return False
            if b == 20:
                if 10 in change_dict and 5 in change_dict and change_dict[10] >= 1 and change_dict[5] >= 1:
                    change_dict[10] -= 1
                    change_dict[5] -= 1
                elif 5 in change_dict and change_dict[5] >= 3:
                    change_dict[5] -= 3
                else:
                    return False

        return True


sol = Solution()
bills = [5,5,10,10,20]
print(sol.lemonadeChange(bills))

bills = [5,5,5,10,20]
print(sol.lemonadeChange(bills))