class Solution:
    def findMaxAverage(self, nums, k):
        currsum,maxsum=0,0
        for i in range(k):
            currsum += nums[i]
        maxsum=currsum
        i=k
        j=0
        while i < len(nums):
            currsum+=nums[i] - nums[j]
            maxsum=max(maxsum,currsum)
            i+=1
            j+=1
        return maxsum/k
    
nums = [1,2,3,4,5]
k = 3
print(Solution().findMaxAverage(nums, k))

#https://leetcode.com/problems/maximum-average-subarray-i/