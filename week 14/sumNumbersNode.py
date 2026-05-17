def sumNumbers(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    stack = [(root, root.val)]
    total = 0
    while stack:
        node, path_sum = stack.pop()
        if not node.left and not node.right:
            total += path_sum
        if node.left:
            stack.append((node.left, path_sum * 10 + node.left.val))
        if node.right:
            stack.append((node.right, path_sum * 10 + node.right.val))
    return total