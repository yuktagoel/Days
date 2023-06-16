class Solution:
    def isValid(self, input):
        s=[]
        d = {'(':')','{':'}','[':']'}
        for i in input:
            if i in [')','}',']']:
                if len(s)==0:   return False
                if(s[-1] in d and d[s[-1]]==i):
                    s.pop()
                else:
                    s.append(i)
            if i in ['(','{','[']:
                s.append(i)
        if len(s)==0:
            return True
        return False
    
s = "()[]{}"
print(Solution().isValid(s))

#https://leetcode.com/problems/valid-parentheses