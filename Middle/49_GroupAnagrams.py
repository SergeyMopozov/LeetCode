"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs):

        # read each word and covert it in dict
        # if each next dict of word already exit add anagram in group
        # return all groups
        dict_anagrams = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k not in dict_anagrams:
                dict_anagrams[k] = []
            dict_anagrams[k].append(s)

        return list(dict_anagrams.values())




sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(sol.groupAnagrams(strs))
