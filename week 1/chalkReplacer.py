def chalkReplacer(self, chalk: list[int], k: int) -> int:
    sum_chalk = sum(chalk)
    k = k % sum_chalk
    for i in range(len(chalk)):
        if k < chalk[i]:
            return i
        k -= chalk[i]