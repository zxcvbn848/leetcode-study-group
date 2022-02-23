# Dynamic Programming
# https://www.bookstack.cn/read/algorithm-exercise-tw/string-longest_palindromic_substring.md#%E9%A1%8C%E8%A7%A31%20-%20%E7%AA%AE%E8%88%89%E6%90%9C%E7%B4%A2(brute%20force)

class Solution:
   def longestPalindrome(self, s: str) -> str:
      n = len(s)
      maxBegin = 0
      maxLen = 1
      table = [[False] * 1000 for i in range(1000)]

      for i in range(n):
         table[i][i] = True
      
      for i in range(n - 1):
         if s[i] == s[i + 1]:
            table[i][i + 1] = True
            maxBegin = i
            maxLen = 2
      
      for length in range(3, n + 1):
         for i in range(0, n - length + 1):
            j = i + length - 1
            if table[i + 1][j - 1] and s[i] == s[j]:
               table[i][j] = True
               if length > maxLen:
                  maxLen = length
                  maxBegin = i
      
      return s[maxBegin : maxBegin + maxLen]

string = "abccbaaaa"
result = Solution().longestPalindrome(string)
print(result)

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
