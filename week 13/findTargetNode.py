def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    if not root:
        return False

    seen = set()
    stack = [root]

    while stack:
        node = stack.pop()

        if k - node.val in seen:
            return True

        seen.add(node.val)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return False