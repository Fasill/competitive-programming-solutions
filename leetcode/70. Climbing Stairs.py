class Solution:
    def climbStairs(self, n: int) -> int:
            c = [1,1]
            i= 1
            while i < n:
                c.append(c[-1]+c[-2])
                i+=1
            return (c[-1])
