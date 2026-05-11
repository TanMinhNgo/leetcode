def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
    graph = [ [[] for _ in range(n)] for _ in range(2) ]
    for u, v in redEdges:
        graph[0][u].append(v)
    for u, v in blueEdges:
        graph[1][u].append(v)

    dist = [[-1] * 2 for _ in range(n)]
    dist[0][0] = dist[0][1] = 0

    queue = deque()
    queue.append((0, 0))  # last color red
    queue.append((0, 1))  # last color blue

    while queue:
        node, color = queue.popleft()
        next_color = 1 - color
        for nei in graph[next_color][node]:
            if dist[nei][next_color] == -1:
                dist[nei][next_color] = dist[node][color] + 1
                queue.append((nei, next_color))

    ans = []
    for r, b in dist:
        if r == -1 and b == -1:
            ans.append(-1)
        elif r == -1:
            ans.append(b)
        elif b == -1:
            ans.append(r)
        else:
            ans.append(min(r, b))
    return ans