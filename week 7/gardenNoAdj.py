def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
    graph = {i: set() for i in range(1, n + 1)}
    for x, y in paths:
        graph[x].add(y)
        graph[y].add(x)

    res = [0] * n
    for i in range(1, n + 1):
        used = {res[j - 1] for j in graph[i]}
        for color in range(1, 5):
            if color not in used:
                res[i - 1] = color
                break

    return res