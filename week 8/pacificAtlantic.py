def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]

    def dfs(i, j, visited):
        visited[i][j] = True
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and heights[x][y] >= heights[i][j]:
                dfs(x, y, visited)

    for i in range(m):
        dfs(i, 0, pacific)
        dfs(i, n - 1, atlantic)
    for j in range(n):
        dfs(0, j, pacific)
        dfs(m - 1, j, atlantic)

    result = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
    return result