class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i]=digits[i] + carry
            carry = digits[i]//10
            digits[i]%=10
        if carry:
            digits.insert(0,carry)
        return digits
    
digits = [9,9,9]
print(Solution().plusOne(digits))

#https://leetcode.com/problems/plus-one/