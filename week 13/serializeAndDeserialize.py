def serialize(self, root: Optional[TreeNode]) -> str:
    if not root:
        return "None"
    return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

def deserialize(self, data: str) -> Optional[TreeNode]:
    if data == "None":
        return None
    vals = iter(data.split(","))

    def build():
        val = next(vals)
        if val == "None":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()