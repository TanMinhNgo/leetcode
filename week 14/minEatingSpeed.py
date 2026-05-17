def minEatingSpeed(self, piles: list[int], h: int) -> int:
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = sum((pile - 1) // mid + 1 for pile in piles)
        if hours > h:
            left = mid + 1
        else:
            right = mid
    return left