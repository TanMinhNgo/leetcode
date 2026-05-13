def closedIsland(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(i: int, j: int) -> bool:
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if grid[i][j] == 1 or visited[i][j]:
            return True

        visited[i][j] = True
        up = dfs(i - 1, j)
        down = dfs(i + 1, j)
        left = dfs(i, j - 1)
        right = dfs(i, j + 1)

        return up and down and left and right

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not visited[i][j]:
                if dfs(i, j):
                    count += 1

    return count