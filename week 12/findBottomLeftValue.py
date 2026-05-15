def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        if node.right:
            queue.append(node.right)
        
        if node.left:
            queue.append(node.left)
    
    return node.val