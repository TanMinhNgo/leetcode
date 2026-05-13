def shortestBridge(self, grid: list[list[int]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 2
        queue.append((i, j))
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    queue = []
    found = False
    for i in range(len(grid)):
        if found:
            break
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                found = True
                break

    steps = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1:
                        return steps
                    elif grid[nx][ny] == 0:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
        steps += 1

    return -1