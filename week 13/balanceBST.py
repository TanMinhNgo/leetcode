def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []

    def build_tree(nums):
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = build_tree(nums[:mid])
        node.right = build_tree(nums[mid + 1:])
        return node

    sorted_vals = inorder(root)
    return build_tree(sorted_vals)