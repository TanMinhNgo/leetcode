def maxProduct(self, root: Optional[TreeNode]) -> int:
    MOD = 10**9 + 7
    subtree_sums = []
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        total = node.val + left + right
        subtree_sums.append(total)
        return total
    
    total_sum = dfs(root)
    best = 0
    for s in subtree_sums[:-1]:
        best = max(best, s * (total_sum - s))
        
    return best % MOD