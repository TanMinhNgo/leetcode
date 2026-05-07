def minAddToMakeValid(self, s: str) -> int:
    left_parentheses = 0
    right_parentheses = 0

    for char in s:
        if char == '(':
            left_parentheses += 1
        elif left_parentheses > 0:
            left_parentheses -= 1
        else:
            right_parentheses += 1

    return left_parentheses + right_parentheses