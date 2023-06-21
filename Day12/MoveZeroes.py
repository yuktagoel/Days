class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        for fast in range(len(nums)):
            if nums[slow]==0 and nums[fast]!=0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow]!=0:
                slow+=1

nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))

#https://leetcode.com/problems/move-zeroes/