class Solution:
    def numberOfSteps(self, num):
        if num ==0 :
            return 0
        if num ==1 :
            return 1
        if num ==2:
            return 2
        if num%2 == 0 :
            return self.numberOfSteps(num//2) + 1
        else:
            return self.numberOfSteps(num-1) + 1
        
n=14
print(Solution().numberOfSteps(n))

#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/