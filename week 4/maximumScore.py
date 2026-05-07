def maximumScore(a: int, b: int, c: int) -> int:
    count = sorted([a, b, c])
    a = count[0]
    b = count[1]
    c = count[2]
    if a + b < c:
        return a + b
    
    return (a + b + c) // 2