# Manacher's algorithm
# https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm

class Solution:
   def longestPalindrome(self, s: str) -> str:
      # 在原字串上添加字符 "#"，使得字串變成回文
      # abba -> ^a#b#b#a$
      S = "#".join("^" + s + "$")
      # 初始化回文的長度
      P = [0] * len(S) # 以 S 每個位置為中心的最長半徑的回文
      # 備註：len(S) = len(P) = 2 * len(s) + 1

      # center 回文的中心點，radius 回文的半徑
      center, radius = 0, 0

      # 檢查每個位置的回文半徑
      for i in range(1, len(S) - 1): # range(1, len(S) - 1)：因為 S 的第一個字元是 ^，最後一個字元是 $
         # 如果 i < right，表示 i 已經被檢查過了，不需要再檢查
         if i < radius:
            P[i] = min(radius - i, P[2 * center - i])

         # 檢查以 i 為中心點，在半徑 P[i] + 1 內是否為回文
         while S[i + P[i] + 1] == S[i - P[i] - 1]:
            # P[i]：該中心點 i 的最長回文半徑
            P[i] += 1

         # 更新回文的中心點及半徑
         if i + P[i] > radius:
            center, radius = i, i + P[i]

      # 最長回文的半徑與中心點索引
      p, idx = max((v, i) for i, v in enumerate(P))

      return s[ (idx - p) // 2 : (idx + p) // 2 ] # // 2 是為了將 # 排除在外

string = "abccbaaaa"
result = Solution().longestPalindrome(string)
print(result)

# Time Complexity: O(N)
# Space Complexity: O(N)