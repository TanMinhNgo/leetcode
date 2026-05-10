def getKth(self, lo: int, hi: int, k: int) -> int:
    def getPower(x):
        if x == 1:
            return 0
        if x % 2 == 0:
            return 1 + getPower(x // 2)
        else:
            return 1 + getPower(3 * x + 1)

    arr = []
    for i in range(lo, hi + 1):
        arr.append((getPower(i), i))
    arr.sort()
    
    return arr[k - 1][1]