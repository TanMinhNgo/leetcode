def flatten(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    stack = [head]
    prev = None

    while stack:
        node = stack.pop()

        if prev:
            prev.next = node
            node.prev = prev

        if node.next:
            stack.append(node.next)
        if node.child:
            stack.append(node.child)
            node.child = None

        prev = node

    return head