class Solution:
    def uniqueOccurrences(self, arr):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        z={}
        for i in d:
            if d[i] in z:
                return False
            else:
                z[d[i]]=1
        return True

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))

#https://leetcode.com/problems/unique-number-of-occurrences