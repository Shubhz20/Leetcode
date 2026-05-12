from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:

            # need extra energy
            if current < minimum:
                extra = minimum - current
                energy += extra
                current += extra

            # do task
            current -= actual

        return energy