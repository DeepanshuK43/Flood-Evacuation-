from collections import deque

def bfs(graph, start, end):
    visited = set()
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return {"path": path, "distance": len(path) - 1}
        elif node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return {"path": [], "distance": float("inf")}
