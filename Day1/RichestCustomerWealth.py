class Solution:
    def maximumWealth(self, accounts) :
        maxwealth = 0
        for i in range(len(accounts)):
            currmax = 0
            for j in range(len(accounts[0])):
                currmax += accounts[i][j]
            maxwealth = max(currmax, maxwealth)
        return maxwealth

accounts = [[1,2,3],[3,2,1]]
print(Solution().maximumWealth(accounts))

#https://leetcode.com/problems/richest-customer-wealth/