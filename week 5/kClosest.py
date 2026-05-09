def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
    points.sort(key=lambda x: x[0]**2 + x[1]**2)
    return points[:k]