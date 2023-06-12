class Solution:
    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False
        mag_dict ={}
        for i in magazine:
            if i in mag_dict:
                mag_dict[i]+=1
            else:
                mag_dict[i]=1
        for i in ransomNote:
            if i not in magazine or mag_dict[i]==0:
                return False
            else:
                mag_dict[i]-=1
        return True
    
ransomNote = "aa"
magazine = "ab"
print(Solution().canConstruct(ransomNote, magazine))

# https://leetcode.com/problems/ransom-note/