class Solution:
    def reverseVowels(self, s):
        dict = "aeiouAEIOU"
        start=0
        news = list(s)
        end=len(s)-1
        while(start<end):
            if news[start] in dict and news[end] in dict:
                news[start],news[end]=news[end],news[start]
                start+=1
                end-=1
            if news[start] not in dict:
                start+=1
            if news[end] not in dict:
                end-=1
        return ''.join(news)

s = "leetcode"
print(Solution().reverseVowels(s))

# https://leetcode.com/problems/reverse-vowels-of-a-string/