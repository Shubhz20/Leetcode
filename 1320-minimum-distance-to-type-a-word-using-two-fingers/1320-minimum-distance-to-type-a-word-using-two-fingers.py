class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1:
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        nums = [ord(c) - ord('A') for c in word]
        n = len(nums)
        
        # dp[j] = min cost when one finger at current, other at j
        dp = [0] * 26
        
        for i in range(1, n):
            new_dp = [float('inf')] * 26
            
            for j in range(26):
                # move same finger
                cost1 = dp[j] + dist(nums[i-1], nums[i])
                new_dp[j] = min(new_dp[j], cost1)
                
                # move other finger
                cost2 = dp[j] + dist(j, nums[i])
                new_dp[nums[i-1]] = min(new_dp[nums[i-1]], cost2)
            
            dp = new_dp
        
        return min(dp)