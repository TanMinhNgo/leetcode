def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)