from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: prefix sums for each column
        # S[j][i] = sum of column j from row 0 to i-1
        S = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                S[j][i+1] = S[j][i] + grid[i][j]
        
        # dp[h_curr][h_prev]
        dp = [[-10**18] * (n + 1) for _ in range(n + 1)]
        
        # base case (first column)
        for h in range(n + 1):
            dp[h][0] = 0
        
        # process columns
        for col in range(1, n):
            new_dp = [[-10**18] * (n + 1) for _ in range(n + 1)]
            
            # precompute suffix max
            suffix_max = [[-10**18] * (n + 2) for _ in range(n + 1)]
            for h_prev in range(n + 1):
                for k in range(n, -1, -1):
                    suffix_max[h_prev][k] = max(
                        suffix_max[h_prev][k+1] if k < n else -10**18,
                        dp[h_prev][k]
                    )
            
            # precompute prefix max
            prefix_max = [[-10**18] * (n + 1) for _ in range(n + 1)]
            for h_prev in range(n + 1):
                best = -10**18
                for k in range(n + 1):
                    val = dp[h_prev][k] - max(0, S[col-1][k] - S[col-1][h_prev])
                    best = max(best, val)
                    prefix_max[h_prev][k] = best
            
            for h_prev in range(n + 1):
                for h_curr in range(n + 1):
                    
                    if h_curr <= h_prev:
                        # case 1
                        val = suffix_max[h_prev][0] + (S[col][h_prev] - S[col][h_curr])
                    
                    else:
                        # case 2
                        val = max(
                            suffix_max[h_prev][h_curr],
                            prefix_max[h_prev][h_curr] + (S[col-1][h_curr] - S[col-1][h_prev])
                        )
                    
                    new_dp[h_curr][h_prev] = val
            
            dp = new_dp
        
        # final answer: last column must be full black or full white
        ans = 0
        for h in range(n + 1):
            ans = max(ans, dp[0][h], dp[n][h])
        
        return ans