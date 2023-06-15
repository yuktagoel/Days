class Solution:
    def reverseWords(self, s):
        l = s.split()
        start=0
        end=len(l)-1
        while(start<end):
            l[start],l[end]=l[end],l[start]
            start+=1
            end-=1
        return " ".join(l)
    
s = "the sky is blue"
print(Solution().reverseWords(s))

# https://leetcode.com/problems/reverse-words-in-a-string/