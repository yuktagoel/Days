class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                count+=1
        if count<n:
            return False
        return True
            
flowerbed = [1,0,0,0,1]
n = 3
print(Solution().canPlaceFlowers(flowerbed, n))

# https://leetcode.com/problems/can-place-flowers/

