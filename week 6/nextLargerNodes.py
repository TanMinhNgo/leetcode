def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    stack = []
    res = []
    i = 0
    while head:
        res.append(0)
        while stack and stack[-1][0] < head.val:
            res[stack[-1][1]] = head.val
            stack.pop()
        stack.append((head.val, i))
        head = head.next
        i += 1
    return res