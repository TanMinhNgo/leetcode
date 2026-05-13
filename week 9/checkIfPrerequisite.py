def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for pre, course in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    reach = [0] * numCourses  # bitset of all prerequisites for each course
    queue = [i for i in range(numCourses) if indegree[i] == 0]
    head = 0

    while head < len(queue):
        node = queue[head]
        head += 1
        for neighbor in graph[node]:
            reach[neighbor] |= reach[node] | (1 << node)
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return [bool((reach[target] >> start) & 1) for start, target in queries]