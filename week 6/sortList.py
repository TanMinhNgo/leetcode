def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    arr = []
    temp = head
    while temp:
        arr.append(temp.val)
        temp = temp.next

    arr.sort()
    temp = head
    i = 0
    while temp:
        temp.val = arr[i]
        temp = temp.next
        i += 1

    return head