class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1 # dp[1]
        prev1 = 2 # dp[2]

        for i in range( 3,n+1):
            tmp = prev1
            prev1 = prev1+prev2
            prev2 = tmp

        return prev1
