from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        last = defaultdict(list)
        ans = float('inf')
        
        for i, val in enumerate(nums):
            last[val].append(i)
            
            # keep only last 3 indices
            if len(last[val]) > 3:
                last[val].pop(0)
            
            if len(last[val]) == 3:
                i1, i2, i3 = last[val]
                ans = min(ans, 2 * (i3 - i1))
        
        return ans if ans != float('inf') else -1