class Solution:
    def isSubsequence(self, s, t):
        slow=0
        fast=0
        while slow<len(s) and fast<len(t):
            if s[slow]==t[fast]:
                slow+=1
            fast+=1
        return len(s)==slow


print(Solution().isSubsequence("abc","ahbgdc"))

# https://leetcode.com/problems/is-subsequence/