def isBipartite(self, graph: list[list[int]]) -> bool:
    n = len(graph)
    color = [0] * n

    def dfs(node, c):
        color[node] = c
        for nei in graph[node]:
            if color[nei] == 0:
                if not dfs(nei, -c):
                    return False
            elif color[nei] == c:
                return False
        return True

    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                return False

    return True