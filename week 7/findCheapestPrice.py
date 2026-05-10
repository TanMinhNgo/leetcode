def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    best = [[float("inf")] * (k + 2) for _ in range(n)]
    best[src][0] = 0

    min_heap = [(0, src, 0)]
    while min_heap:
        cost, node, stops = heapq.heappop(min_heap)
        if node == dst:
            return cost
        if stops == k + 1:
            continue
        if cost > best[node][stops]:
            continue

        for neighbor, price in graph[node]:
            new_cost = cost + price
            if new_cost < best[neighbor][stops + 1]:
                best[neighbor][stops + 1] = new_cost
                heapq.heappush(min_heap, (new_cost, neighbor, stops + 1))

    return -1