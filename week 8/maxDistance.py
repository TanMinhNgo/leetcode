def maxDistance(self, grid: list[list[int]]) -> int:
    n = len(grid)
    queue = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j))

    if not queue or len(queue) == n * n:
        return -1

    max_dist = -1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                max_dist = max(max_dist, grid[nx][ny] - 1)
                queue.append((nx, ny))

    return max_dist