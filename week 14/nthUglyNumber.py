def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
    def lcm(x: int, y: int) -> int:
        from math import gcd
        return x * y // gcd(x, y)

    def countUglyNumbers(x: int) -> int:
        return x // a + x // b + x // c - x // lcm(a, b) - x // lcm(a, c) - x // lcm(b, c) + x // lcm(lcm(a, b), c)

    left, right = 1, 2 * 10**9
    while left < right:
        mid = (left + right) // 2
        if countUglyNumbers(mid) < n:
            left = mid + 1
        else:
            right = mid
    return left