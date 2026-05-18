def clumsy(self, n: int) -> int:
    stack = [n]
    n -= 1
    index = 0
    while n > 0:
        if index % 4 == 0:
            stack[-1] = int(stack[-1] * n)
        elif index % 4 == 1:
            stack[-1] = int(stack[-1] / n)
        elif index % 4 == 2:
            stack.append(n)
        else:
            stack.append(-n)
        n -= 1
        index += 1
    return sum(stack)