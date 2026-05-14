def minSwapsCouples(self, row: list[int]) -> int:
    n = len(row)
    pos = [0] * n
    for i in range(n):
        pos[row[i]] = i

    swaps = 0
    for i in range(0, n, 2):
        x = row[i]
        y = x ^ 1
        if row[i + 1] != y:
            swaps += 1
            j = pos[y]
            row[i + 1], row[j] = row[j], row[i + 1]
            pos[row[j]] = j
            pos[row[i + 1]] = i + 1

    return swaps