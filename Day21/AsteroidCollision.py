class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        return stack

asteroids = [-2, -1, 1, 2]
print(Solution().asteroidCollision(asteroids))

#https://leetcode.com/problems/asteroid-collision