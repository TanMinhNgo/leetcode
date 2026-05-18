def sampleStats(self, count: list[int]) -> list[float]:
    total = sum(count)
    if total == 0:
        return [0.0, 0.0, 0.0, 0.0, 0.0]

    min_val = next(i for i, c in enumerate(count) if c > 0)
    max_val = next(i for i in range(255, -1, -1) if count[i] > 0)

    mean = sum(i * c for i, c in enumerate(count)) / total

    mid1 = (total + 1) // 2
    mid2 = (total + 2) // 2
    cumulative = 0
    m1 = m2 = 0
    for i, c in enumerate(count):
        cumulative += c
        if cumulative >= mid1 and m1 == 0:
            m1 = i
        if cumulative >= mid2:
            m2 = i
            break
    median = (m1 + m2) / 2

    mode = max(range(256), key=lambda i: count[i])

    return [float(min_val), float(max_val), mean, float(median), float(mode)]
