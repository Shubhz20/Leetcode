from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):

            vals = []
            pos = []

            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            # top row
            for j in range(left, right):
                vals.append(grid[top][j])
                pos.append((top, j))

            # right column
            for i in range(top, bottom):
                vals.append(grid[i][right])
                pos.append((i, right))

            # bottom row
            for j in range(right, left, -1):
                vals.append(grid[bottom][j])
                pos.append((bottom, j))

            # left column
            for i in range(bottom, top, -1):
                vals.append(grid[i][left])
                pos.append((i, left))

            length = len(vals)

            rot = k % length

            # counter-clockwise rotation
            rotated = vals[rot:] + vals[:rot]

            for idx in range(length):
                r, c = pos[idx]
                grid[r][c] = rotated[idx]

        return grid