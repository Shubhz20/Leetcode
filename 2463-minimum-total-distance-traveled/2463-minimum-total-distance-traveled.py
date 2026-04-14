from typing import List
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        @lru_cache(None)
        def solve(i, j):
            # all robots assigned
            if i == n:
                return 0
            
            # no factories left
            if j == m:
                return float('inf')
            
            res = float('inf')
            pos, limit = factory[j]
            
            # Option 1: skip this factory
            res = solve(i, j + 1)
            
            # Option 2: assign k robots to this factory
            total_dist = 0
            for k in range(1, limit + 1):
                if i + k - 1 >= n:
                    break
                
                # add distance of k-th robot
                total_dist += abs(robot[i + k - 1] - pos)
                
                res = min(res, total_dist + solve(i + k, j + 1))
            
            return res
        
        return solve(0, 0)