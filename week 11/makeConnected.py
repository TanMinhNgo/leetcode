def makeConnected(self, n: int, connections: list[list[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    graph = {i: [] for i in range(n)}
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1

    return components - 1