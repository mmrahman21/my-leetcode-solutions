class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [[0]*3 for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = 1, 0, 1
        
        for i in range(1, n):
            for lane in range(3):
                if obstacles[i] == lane+1:
                    dp[i][lane] = n+1
                else:
                    p = dp[i-1][(lane+1) % 3] if obstacles[i] != (lane+1) % 3 + 1 else n
                    q = dp[i-1][(lane + 2) % 3] if obstacles[i] != (lane + 2) % 3 + 1 else n
                    dp[i][lane] = min(dp[i-1][lane], p + 1, q + 1)
        
        return min(dp[-1])
    