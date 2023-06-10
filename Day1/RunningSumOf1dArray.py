class Solution:
    def runningSum(self, nums) :
        currsum=nums[0]
        for i in range(1,len(nums)):
            currsum+=nums[i]
            nums[i]=currsum
        return nums

nums = [1,2,3,4]
print(Solution().runningSum(nums))

#https://leetcode.com/problems/running-sum-of-1d-array/
