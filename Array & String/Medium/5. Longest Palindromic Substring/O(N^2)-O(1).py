# Expand around center
# 共有 2n - 1 個中心點需檢查
# 比如 abba，共有 7 個中心點，分別為 a, ab 之間, b, bb 之間, b, ba 之間, a

class Solution:
   def longestPalindrome(self, s: str) -> str:
      # 設定 start 和 end 為最長回文的左右邊界
      start, end = 0, 0
      # i 和 j 分別為中心點的左右 index
      i, j = 0, 0

      while j < len(s):
         left, right = i, j

         # 在 s 的字串總長內，如果 s[left] == s[right]，
         # 則 left 往左移動，right 往右移動
         while left >= 0 and right < len(s) and s[left] == s[right]:
            print("right - left: ", right - left, " || end - start: ", end - start)
            # 如果檢查到的左右邊界的差異大於現有的最長回文長度，則更新最長回文的左右邊界
            if right - left > end - start:
               start, end = left, right
            left -= 1
            right += 1

            print("start: ", start, " || end: ", end)
            print("-------------------")

         # 中心點位置變化
         if i == j:
            j += 1
         else:
            i += 1

      return s[ start : end + 1 ]

string = "abccbaaaa"
result = Solution().longestPalindrome(string)
print(result)

# Time Complexity: O(N^2)
# Space Complexity: O(1)
