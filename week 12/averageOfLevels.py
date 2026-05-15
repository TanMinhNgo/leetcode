def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level_sum = 0
        level_count = len(queue)
        for _ in range(level_count):
            node = queue.pop(0)
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_count)
    return result