def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
    pairs = []

    for i in range(len(quality)):
        pairs.append((wage[i]/quality[i], quality[i]))
    pairs.sort(key = lambda p : p[0])

    heap = []
    res = float('inf')
    total_quality = 0
    for rate, q in pairs:
        heapq.heappush(heap, -q)
        total_quality += q

        if len(heap) > k:
            total_quality += heapq.heappop(heap)
        
        if len(heap) == k:
            res = min(res, total_quality * rate)
        
    return res