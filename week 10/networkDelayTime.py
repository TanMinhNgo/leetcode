def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        current_dist, node = heapq.heappop(heap)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    max_dist = max(dist.values())
    return max_dist if max_dist != float('inf') else -1