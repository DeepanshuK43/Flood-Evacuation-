import heapq

def dijkstra(graph, start, end):
    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if u == end:
            break
        for v, weight in graph[u].items():
            alt = curr_dist + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    path = []
    node = end
    while node:
        path.insert(0, node)
        node = prev[node]
    return {"path": path, "distance": dist[end]}
