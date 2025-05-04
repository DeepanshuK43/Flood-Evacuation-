import heapq

def dijkstra(graph, start, end):
    # Priority queue: stores tuples of (distance, node)
    queue = [(0, start)]
    # Distances dictionary stores shortest path distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Path dictionary stores the actual path
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # If we reach the end node, break
        if current_node == end:
            break

        for neighbor, data in graph[current_node].items():
            # Use both distance and flood-risk as factors
            total_distance = current_distance + data["distance"] + data["flood-risk"]
            
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (total_distance, neighbor))

    # Reconstruct the path
    path = []
    current_node = end
    while current_node:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    # Return the result as a dictionary
    return {
        "distance": distances[end],
        "path": path
    }
