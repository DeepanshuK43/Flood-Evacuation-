import heapq

def heuristic(a, b):
    return abs(ord(a) - ord(b))

def astar(graph, start, end):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current:
                path.insert(0, current)
                current = came_from.get(current)
            return {"path": path, "distance": g_score[end]}
        
        for neighbor, weight in graph[current].items():
            tentative = g_score[current] + weight
            if tentative < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score = tentative + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score, neighbor))
    
    return {"path": [], "distance": float("inf")}
