def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node, sum_so_far):
        if not node:
            return sum_so_far
        sum_so_far = dfs(node.right, sum_so_far)
        node.val += sum_so_far
        sum_so_far = node.val
        return dfs(node.left, sum_so_far)

    dfs(root, 0)
    return root