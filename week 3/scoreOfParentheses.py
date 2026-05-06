def scoreOfParentheses(self, s: str) -> int:
    stack = []
    current_score = 0
    for char in s:
        if char == '(':
            stack.append(current_score)
            current_score = 0
        else:
            if current_score == 0:
                current_score = 1
            else:
                current_score *= 2
            current_score += stack.pop()
            
    return current_score