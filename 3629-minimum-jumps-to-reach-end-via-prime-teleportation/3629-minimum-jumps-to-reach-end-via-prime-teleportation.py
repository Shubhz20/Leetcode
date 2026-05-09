from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        mx = max(nums)

        # SPF sieve
        spf = list(range(mx + 1))

        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # check prime
        def is_prime(x):
            return x >= 2 and spf[x] == x

        # Build:
        # prime -> indices divisible by prime
        divisible = defaultdict(list)

        for i, x in enumerate(nums):
            temp = x
            seen = set()

            while temp > 1:
                p = spf[temp]

                if p not in seen:
                    divisible[p].append(i)
                    seen.add(p)

                while temp % p == 0:
                    temp //= p

        # BFS
        q = deque([(0, 0)])
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        while q:
            i, d = q.popleft()

            if i == n - 1:
                return d

            # adjacent
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    q.append((ni, d + 1))

            # teleport
            val = nums[i]

            if is_prime(val) and val not in used_prime:
                for ni in divisible[val]:
                    if not visited[ni]:
                        visited[ni] = True
                        q.append((ni, d + 1))

                used_prime.add(val)

        return -1