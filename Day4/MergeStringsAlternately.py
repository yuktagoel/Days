class Solution:
    def mergeAlternately(self, word1, word2):
        ans=''
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        for i,j in zip(word1,word2):
            ans=ans+i
            ans+=j
        count = len(word1)-len(word2)
        if(count<0):
            ans+=word2[len(word2)-abs(count):]
        if(count>0):
            ans+=word1[len(word1)-abs(count):]
        return ans
    
word1 = "ab"
word2 = "pq"
print(Solution().mergeAlternately(word1, word2))

# https://leetcode.com/problems/merge-strings-alternately/