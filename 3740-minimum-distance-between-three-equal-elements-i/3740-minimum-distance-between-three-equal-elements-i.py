from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        # store indices
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = float('inf')
        
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # check consecutive triples
            for i in range(len(indices) - 2):
                left = indices[i]
                right = indices[i + 2]
                
                dist = 2 * (right - left)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1