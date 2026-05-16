def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
        return
    
    dfs(root1)
    dfs(root2)
    return sorted(res)