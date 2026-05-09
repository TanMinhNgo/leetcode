def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
    low, high = matrix[0][0], matrix[-1][-1]

    while low < high:
        mid = low + (high - low) // 2
        count = 0

        c = len(matrix[0]) - 1
        for r in range(len(matrix)):
            while c >= 0 and matrix[r][c] > mid:
                c -= 1
            count += (c + 1)

            if count < k:
                low = mid + 1
            else:
                high = mid

    return low