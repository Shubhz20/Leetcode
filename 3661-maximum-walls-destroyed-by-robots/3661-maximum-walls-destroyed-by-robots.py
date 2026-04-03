from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Step 1: sort robots
        robots_data = sorted(zip(robots, distance))
        robots = [r for r, _ in robots_data]
        dist = [d for _, d in robots_data]
        walls.sort()
        
        n = len(robots)
        m = len(walls)
        
        # helper function
        def count_range(l, r):
            import bisect
            if l > r:
                return 0
            return bisect.bisect_right(walls, r) - bisect.bisect_left(walls, l)
        
        # Step 2: precompute
        leftWall = [0]*n
        rightWall = [0]*n
        common = [0]*n
        
        for i in range(n):
            r = robots[i]
            d = dist[i]
            
            prev_r = robots[i-1] if i > 0 else -10**18
            next_r = robots[i+1] if i < n-1 else 10**18
            
            # LEFT
            L = max(prev_r + 1, r - d)
            R = r
            leftWall[i] = count_range(L, R)
            
            # RIGHT
            L = r
            R = min(next_r - 1, r + d)
            rightWall[i] = count_range(L, R)
        
        # common overlap
        for i in range(1, n):
            prev = robots[i-1]
            curr = robots[i]
            
            L = max(prev + 1, curr - dist[i])
            R = min(curr - 1, prev + dist[i-1])
            
            if L <= R:
                common[i] = count_range(L, R)
        
        # Step 3: DP
        dpL = leftWall[0]
        dpR = rightWall[0]
        
        for i in range(1, n):
            newL = leftWall[i] + max(dpL, dpR - common[i])
            newR = rightWall[i] + max(dpL, dpR)
            
            dpL, dpR = newL, newR
        
        return max(dpL, dpR)