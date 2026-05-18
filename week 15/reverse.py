def reverse(self, x: int) -> int:
    sign = 1 if x >= 0 else -1
    x = abs(x)
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    return sign * result if -2**31 <= sign * result <= 2**31 - 1 else 0