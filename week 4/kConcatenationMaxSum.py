def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
    mod = 10 ** 9 + 7

    def kadane(nums: list[int]) -> int:
        best = 0
        curr = 0
        for x in nums:
            curr = max(0, curr + x)
            best = max(best, curr)
        return best

    total_sum = sum(arr)
    if k == 1:
        return kadane(arr) % mod

    best = kadane(arr * 2)
    if total_sum > 0 and k > 2:
        best += (k - 2) * total_sum

    return best % mod