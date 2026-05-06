def removeDuplicates(self, s: str) -> str:
    if len(s) < 2:
        return ""
    
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)