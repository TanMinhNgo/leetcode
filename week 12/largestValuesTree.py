def largestValuesTree(self, root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    
    queue = [root]
    result = []
    
    while queue:
        level_size = len(queue)
        max_value = float('-inf')
        
        for _ in range(level_size):
            node = queue.pop(0)
            max_value = max(max_value, node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(max_value)
    
    return result