class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left = mid +1
            else:
                right = mid - 1

        return left

        
nums = [1,3,5,6]
print(Solution().searchInsert(nums, 7))

