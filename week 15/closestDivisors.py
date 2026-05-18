def closestDivisors(self, num: int) -> list[int]:
    for i in range(math.isqrt(num + 2), 0, -1):
        if (num + 1) % i == 0:
            return [i, (num + 1) // i]
        if (num + 2) % i == 0:
            return [i, (num + 2) // i]