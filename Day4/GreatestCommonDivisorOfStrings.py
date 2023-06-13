class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 == str2:
            return str1
        if(str1+str2 != str2+str1):
            return ''
        if(len(str1)>len(str2)):
            return self.gcdOfStrings(str1[len(str2):] , str2)
        if(len(str2)>len(str1)):
            return self.gcdOfStrings(str2[len(str1):] , str1)
        
str1 = "ABCABC"
str2 = "ABC"
print(Solution().gcdOfStrings(str1, str2))

# https://leetcode.com/problems/greatest-common-divisor-of-strings/