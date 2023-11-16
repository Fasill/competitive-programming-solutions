class Solution(object):
    def isAnagram(self, s, t):
        # Check if the lengths of the input strings are not equal, which means they can't be anagrams.
        if len(s) != len(t):
            return False
        
        # Sort the characters in both strings.
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        # Compare the sorted strings to determine if they are anagrams.
        return sorted_t == sorted_s
