def dfs(graph, start, end, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    
    if start == end:
        return {"path": path, "distance": len(path) - 1}
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, path[:], visited.copy())
            if result["path"]:
                return result

    return {"path": [], "distance": float("inf")}
