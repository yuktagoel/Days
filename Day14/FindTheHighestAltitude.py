class Solution:
    def largestAltitude(self, gain):
        currsum=0
        maxsum=currsum
        for i in gain:
            currsum+=i
            maxsum=max(currsum,maxsum)
        return maxsum
    
print(Solution().largestAltitude([-5,1,5,0,-7]))
