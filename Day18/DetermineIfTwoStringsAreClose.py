class Solution:
    def closeStrings(self, word1, word2):
        if (len(word1)) != len(word2):
            return False
        d={}
        for i in word1:
            if i not in word2:
                return False
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        z={}
        for i in word2:
            if i not in word1:
                return False
            if i in z:
                z[i]+=1
            else:
                z[i]=1
        if d==z:
            return True
        ans1,ans2=[],[]
        for i in d:
            ans1.append(d[i])
        for i in z:
            ans2.append(z[i])
        if sorted(ans1) == sorted(ans2):
            return True
        return False
        
print(Solution().closeStrings("abc","bca"))