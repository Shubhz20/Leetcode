from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        n = len(nums)

        # extra size to avoid boundary issues
        diff = [0] * (2 * limit + 5)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # default = 2 moves
            diff[2] += 2

            # 1 move range
            diff[low] -= 1
            diff[high + 1] += 1

            # 0 move at exact sum
            diff[s] -= 1
            diff[s + 1] += 1

        ans = float('inf')
        curr = 0

        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)

        return ans