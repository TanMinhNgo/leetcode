def baseNeg2(self, n: int) -> str:
    if n == 0:
        return '0'
    result = []
    while n != 0:
        n, remainder = divmod(n, -2)
        if remainder < 0:
            n += 1
            remainder += 2
        result.append(str(remainder))
    return ''.join(reversed(result))