def canReach(self, arr: list[int], start: int) -> bool:
    visited = set()
    stack = [start]

    while stack:
        index = stack.pop()
        if index < 0 or index >= len(arr) or index in visited:
            continue
        if arr[index] == 0:
            return True
        visited.add(index)
        stack.append(index + arr[index])
        stack.append(index - arr[index])

    return False