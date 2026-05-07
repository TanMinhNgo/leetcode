def minSetSize(self, arr: list[int]) -> int:
    count = Counter(arr)
    sorted_counts = sorted(count.values(), reverse=True)
    total_removed = 0
    set_size = 0

    for c in sorted_counts:
        total_removed += c
        set_size += 1
        if total_removed >= len(arr) // 2:
            break

    return set_size