from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        
        # Step 1: Build components
        for a, b in allowedSwaps:
            union(a, b)
        
        # Step 2: Group indices by component
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)
        
        # Step 3: Calculate min Hamming distance
        ans = 0
        
        for indices in groups.values():
            count = Counter()
            
            # count source values
            for i in indices:
                count[source[i]] += 1
            
            # match with target
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    ans += 1
        
        return ans