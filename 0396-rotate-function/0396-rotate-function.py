from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        
        total_sum = sum(nums)
        
        # compute F(0)
        F = sum(i * num for i, num in enumerate(nums))
        max_val = F
        
        # compute other F(k)
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)
        
        return max_val