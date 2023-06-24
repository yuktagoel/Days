class Solution:
    def removeStars(self, s):
        temp=[]
        for i in range(len(s)):
            if s[i]!= '*':
                temp.append(s[i])
            else:
                if len(temp)>0:
                    temp.pop()
        return ''.join(temp)
    
s = "leet**cod*e"
print(Solution().removeStars(s))

#https://leetcode.com/problems/removing-stars-from-a-string