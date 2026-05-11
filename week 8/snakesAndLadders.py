def snakesAndLadders(self, board: list[list[int]]) -> int:
    n = len(board)
    moves = [0] * (n * n + 1)
    idx = 1
    for i in range(n - 1, -1, -1):
        for j in range(n):
            moves[idx] = board[i][j]
            idx += 1
        if (n - i) % 2 == 0:
            moves[idx - n:idx] = reversed(moves[idx - n:idx])

    visited = set()
    queue = deque([(1, 0)])
    while queue:
        pos, steps = queue.popleft()
        if pos == n * n:
            return steps
        for i in range(1, 7):
            next_pos = pos + i
            if next_pos <= n * n:
                next_pos = moves[next_pos] if moves[next_pos] != -1 else next_pos
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, steps + 1))
                    
    return -1