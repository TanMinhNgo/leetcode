def isValidSerialization(self, preorder: str) -> bool:
    stack = []
    for node in preorder.split(','):
        while node == '#' and stack and stack[-1] == '#':
            stack.pop()
            if not stack:
                return False
            stack.pop()
        stack.append(node)
    return len(stack) == 1 and stack[0] == '#'