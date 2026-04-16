from typing import List
import bisect
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: store indices of each value
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = []
        
        for q in queries:
            value = nums[q]
            indices = pos[value]
            
            # If only one occurrence
            if len(indices) == 1:
                res.append(-1)
                continue
            
            # Binary search position
            idx = bisect.bisect_left(indices, q)
            
            # Check neighbors (circular in indices list)
            left = indices[idx - 1] if idx > 0 else indices[-1]
            right = indices[idx + 1] if idx < len(indices) - 1 else indices[0]
            
            # Compute circular distances
            d1 = min(abs(q - left), n - abs(q - left))
            d2 = min(abs(q - right), n - abs(q - right))
            
            res.append(min(d1, d2))
        
        return res