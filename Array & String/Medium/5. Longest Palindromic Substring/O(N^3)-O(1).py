# Brute Force

class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        longest, left, right = 0, 0, 0
        for i in range(0, n):
            for j in range(i + 1, n + 1): # n (n - 1) / 2 個 substrings
                substr = s[i:j]
                if self.isPalindrome(substr) and len(substr) > longest:
                    longest = len(substr)
                    left, right = i, j
        # construct longest substr
        result = s[left:right]
        return result

    def isPalindrome(self, s):
        if not s:
            return False
        # reverse compare
        return s == s[::-1] # 最多執行 n 次


string = "abccbaaaa"
result = Solution().longestPalindrome(string)
print(result)

# Time Complexity: O(N^3)
# Space Complexity: O(1)