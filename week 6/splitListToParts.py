def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    total_nodes = 0
    current = head
    while current:
        total_nodes += 1
        current = current.next

    part_size = total_nodes // k
    extra_nodes = total_nodes % k

    parts = []
    current = head

    for i in range(k):
        parts.append(current)
        current_part_size = part_size + (1 if i < extra_nodes else 0)

        for j in range(current_part_size - 1):
            if current:
                current = current.next

        if current:
            next_part_head = current.next
            current.next = None
            current = next_part_head

    return parts