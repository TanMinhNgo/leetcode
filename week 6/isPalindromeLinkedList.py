def isPalindrome(self, head: Optional[ListNode]) -> bool:
    nums = []

    while head:
        nums.append(head.val)
        head = head.next
        
    return nums == nums[::-1]