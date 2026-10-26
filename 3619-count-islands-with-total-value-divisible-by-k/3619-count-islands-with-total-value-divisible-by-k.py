class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = grid[i][j]
                    grid[i][j] = 0
                    stack = [(i, j)]

                    while stack:
                        r, c = stack.pop()
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                total += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    if total % k == 0:
                        ans += 1
        return ans