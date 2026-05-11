def openLock(self, deadends: list[str], target: str) -> int:
    dead = set(deadends)
    if '0000' in dead:
        return -1
    queue = deque([('0000', 0)])
    while queue:
        node, step = queue.popleft()
        if node == target:
            return step
        for i in range(4):
            for d in (-1, 1):
                y = (int(node[i]) + d) % 10
                nei = node[:i] + str(y) + node[i + 1:]
                if nei not in dead:
                    dead.add(nei)
                    queue.append((nei, step + 1))
    return -1