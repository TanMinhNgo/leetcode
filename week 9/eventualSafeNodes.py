def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
    n = len(graph)
    state = [0] * n
    
    def dfs(node):
        if state[node] != 0:
            return state[node] == 2

        state[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False

        state[node] = 2
        return True
    
    res = []
    for i in range(n):
        if dfs(i):
            res.append(i)
    
    return res