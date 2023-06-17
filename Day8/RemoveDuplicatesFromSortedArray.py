class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        curr = 0
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[count]=nums[i]
                count+=1
        return count


nums = [1,1,2]
print(Solution().removeDuplicates(nums))


#https://leetcode.com/problems/remove-duplicates-from-sorted-array/