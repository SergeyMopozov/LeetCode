"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have
a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.
"""

class Solution:
    def findRestaurant(self, list1, list2):
        least_index = {}
        for w in list1:
            if w in list2:
                if list1.index(w)+list2.index(w) not in least_index:
                    least_index[list1.index(w)+list2.index(w)] = []
                least_index[list1.index(w)+list2.index(w)].append(w)

        return least_index[min(least_index.keys())]



sol = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]

print(sol.findRestaurant(list1, list2))

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(sol.findRestaurant(list1, list2))
