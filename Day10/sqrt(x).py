class Solution:
    def mySqrt(self, x) :
        if x<2:
            return x
        guess=x/2
        while(True):
            new_guess = (guess + x/guess) / 2
            if abs(guess-new_guess) < 1 :
                return floor(abs(new_guess))
            else:
                guess = new_guess


print(Solution().mySqrt(8)) 

#https://leetcode.com/problems/sqrtx/