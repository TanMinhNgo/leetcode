def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
    graph = defaultdict(list)

    def build_graph(node, parent):
        if node:
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

    build_graph(root, None)

    visited = set()
    visited.add(target.val)
    queue = deque([(target.val, 0)])
    result = []

    while queue:
        node_val, dist = queue.popleft()
        if dist == k:
            result.append(node_val)
        elif dist < k:
            for neighbor in graph[node_val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

    return result