class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        # Initialize the array
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # Fill in the array
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    

s = Solution()

l = s.climbStairs(45)
print(l)