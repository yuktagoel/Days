class Solution:
    def removeElement(self, nums, val):
        if val not in nums:
            return len(nums)
        start=0
        end=len(nums)-1
        while(end>=start):
            if nums[start]==val and nums[end]!=val:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
            if nums[start]!=val:
                start+=1
            if nums[end]==val:
                end-=1
        return start
            
nums = [3,2,2,3]
val = 3
print(nums[:Solution().removeElement(nums, val)])

#https://leetcode.com/problems/remove-element/