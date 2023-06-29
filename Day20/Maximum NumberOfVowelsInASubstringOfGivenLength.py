class Solution:
    def maxVowels(self, s, k):
        currvow=0
        maxvow=0
        d=['a','e','i','o','u']
        for i in range(k):
            if s[i] in d:
                currvow+=1
        maxvow=currvow

        i = k
        j=0
        while(i<len(s)):
            if s[i] in d:
                currvow+=1
            if s[j] in d:
                currvow-=1
            maxvow=max(maxvow,currvow)
            i+=1
            j+=1
            
        return maxvow
    
s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))