def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    
    right_view = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        right_view.append(queue[-1].val)
        
        for _ in range(level_size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return right_view