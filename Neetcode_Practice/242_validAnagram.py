class Solution:
    def isAnagram(self, s, t):
        # check if both strs of same length
        if len(s) != len(t):
            return False
        
        # declare an empty dictionary to keep track of alphabet count
        count_s = {}
        
        # Insert an element to the dict if not available otherwise increase the count of element
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
        
        # Check if char in t is available in s
        for i in t:
            if i in count_s:
                count_s[i] = count_s[i] - 1
        
        # If all the values in the dictionary count_s is 0, it means t is an anagram of s
        for val in count_s.values():
            if val != 0:
                return False
        return True