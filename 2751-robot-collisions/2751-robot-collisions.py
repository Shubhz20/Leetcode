from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(n)]
        )
        
        stack = []  # store indices of robots in 'robots' list
        alive = [True] * n
        health = [robots[i][1] for i in range(n)]
        
        for i in range(n):
            pos, h, d, idx = robots[i]
            
            if d == 'R':
                stack.append(i)
            else:
                # process collisions
                while stack and health[i] > 0:
                    j = stack[-1]
                    
                    if health[j] < health[i]:
                        # R robot dies
                        alive[j] = False
                        stack.pop()
                        health[i] -= 1
                    elif health[j] > health[i]:
                        # L robot dies
                        alive[i] = False
                        health[j] -= 1
                        break
                    else:
                        # both die
                        alive[j] = False
                        alive[i] = False
                        stack.pop()
                        break
        
        # collect survivors in original order
        result = []
        for i in range(n):
            if alive[i]:
                result.append((robots[i][3], health[i]))
        
        # sort by original index
        result.sort()
        
        return [h for _, h in result]