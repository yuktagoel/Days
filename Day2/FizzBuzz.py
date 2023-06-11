class Solution:
    def fizzBuzz(self, n):
        zum=[]
        for i in range(1,n+1):
            if i%5==0 and i%3==0:
                zum.append("FizzBuzz")
            elif i%5==0 :
                zum.append("Buzz")
            elif i%3==0:
                zum.append("Fizz")
            else:
                zum.append(str(i))
        return zum

n = 3
print(Solution().fizzBuzz(n))

#https://leetcode.com/problems/fizz-buzz/