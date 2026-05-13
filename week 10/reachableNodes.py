def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append((v, c + 1))
        adj[v].append((u, c + 1))
    
    minMoves = [float('inf')] * n
    minMoves[0] = 0
    heap = [(0, 0)]
    while heap:
        cur_m, u = heappop(heap)
        if cur_m > minMoves[u]: continue
        for v, moves_to_v in adj[u]:
            new_m = moves_to_v + cur_m
            if new_m <= maxMoves and new_m < minMoves[v]:
                minMoves[v] = new_m
                heappush(heap, (new_m, v))
    good = sum((minMoves[i] != float('inf')) for i in range(n))
    
    for u, v, c in edges:
        reachable_from_u = max(0, maxMoves - minMoves[u])
        reachable_from_v = max(0, maxMoves - minMoves[v])

        good += min(c, reachable_from_u + reachable_from_v)
    return good