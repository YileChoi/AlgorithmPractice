class Solution(object):
    def isAnagram(self, s, t):
      result = False
      anagram_list1 = []
      anagram_list2 = []
      if len(s) != len(t):
        return False
      else:
        for i in range(0, len(s)):
          anagram_list1 += s[i]
          anagram_list2 += t[i]

        anagram_list1.sort()
        anagram_list2.sort()

        for i in range(0, len(anagram_list1)):
          if anagram_list1[i] != anagram_list2[i]:
            result = False
            break
          else:
            result = True
      return result