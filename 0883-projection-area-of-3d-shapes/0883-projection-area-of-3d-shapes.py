class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        xy = yz = zx = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    xy+=1

        for box in grid:
            zx +=max(box)

        for j in range(len(grid)):
            yz += max(grid[i][j] for i in range(len(grid)))

        return xy+yz+zx