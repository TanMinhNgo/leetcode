def matrixReshape(self, nums: list[list[int]], r: int, c: int) -> list[list[int]]:
    if len(nums) * len(nums[0]) != r * c:
        return nums

    reshaped = [[0] * c for _ in range(r)]
    row, col = 0, 0

    for i in range(len(nums)):
        for j in range(len(nums[0])):
            reshaped[row][col] = nums[i][j]
            col += 1

            if col == c:
                col = 0
                row += 1

    return reshaped