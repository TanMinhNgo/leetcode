def countPaths(self, n: int, roads: list[list[int]]) -> int:
    import heapq

    mod = 1_000_000_007
    graph = [[] for _ in range(n)]
    for u, v, time in roads:
        graph[u].append((v, time))
        graph[v].append((u, time))

    dist = [float("inf")] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    heap = [(0, 0)]

    while heap:
        current_dist, node = heapq.heappop(heap)
        if current_dist > dist[node]:
            continue
        for neighbor, time in graph[node]:
            new_dist = current_dist + time
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                ways[neighbor] = ways[node]
                heapq.heappush(heap, (new_dist, neighbor))
            elif new_dist == dist[neighbor]:
                ways[neighbor] = (ways[neighbor] + ways[node]) % mod

    return ways[n - 1] % mod