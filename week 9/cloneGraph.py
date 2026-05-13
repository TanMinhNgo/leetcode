def cloneGraph(self, node: 'Node') -> Optional['Node']:
    if not node:
        return None

    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node)