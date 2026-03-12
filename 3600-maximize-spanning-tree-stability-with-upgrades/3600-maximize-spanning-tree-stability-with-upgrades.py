from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        def can(x):
            dsu = DSU(n)
            upgrades = 0
            count = 0

            # first process mandatory edges
            for u,v,s,m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if dsu.union(u,v):
                        count += 1
                    else:
                        return False   # cycle

            # optional edges
            temp = []

            for u,v,s,m in edges:
                if m == 0:
                    if s >= x:
                        temp.append((0,u,v))
                    elif s*2 >= x:
                        temp.append((1,u,v))

            temp.sort()

            for cost,u,v in temp:
                if dsu.union(u,v):
                    upgrades += cost
                    count += 1
                    if upgrades > k:
                        return False
                    if count == n-1:
                        return True

            return count == n-1


        left, right = 1, max(s for _,_,s,_ in edges)*2
        ans = -1

        while left <= right:
            mid = (left + right)//2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans