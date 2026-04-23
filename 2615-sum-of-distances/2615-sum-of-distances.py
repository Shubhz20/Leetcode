from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        
        # Step 1: store indices
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = [0] * len(nums)
        
        # Step 2: process each group
        for indices in pos.values():
            n = len(indices)
            
            # prefix sum of indices
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            
            for i in range(n):
                idx = indices[i]
                
                # left contribution
                left = idx * i - prefix[i]
                
                # right contribution
                right = (prefix[n] - prefix[i + 1]) - idx * (n - i - 1)
                
                res[idx] = left + right
        
        return res