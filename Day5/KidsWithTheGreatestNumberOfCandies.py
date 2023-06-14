class Solution:
    def kidsWithCandies(self, candies, n):
        maxGreatest = max([(i) for i in candies])
        for i in range(len(candies)):
            currGreatest = candies[i] + n 
            print(currGreatest)
            if currGreatest >= maxGreatest:
                candies[i]=True
            else:
                candies[i]=False
        return candies
    
candies = [2,3,5,1,3]
n = 3
print(Solution().kidsWithCandies(candies, n))

#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/