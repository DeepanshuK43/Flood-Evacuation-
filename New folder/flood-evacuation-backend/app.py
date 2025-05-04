import json
from flask import Flask, request, jsonify
from algorithms.dijkstra import dijkstra
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Function to load the graph data from a JSON file
def load_graph_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load the graph from the 'data/graph.json' file
graph = load_graph_from_json('data/graph.json')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Server is running!"}), 200

@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.get_json()
    start = data.get('start')
    end = data.get('end')

    logging.info(f"Request received: start={start}, end={end}")

    # Check if start and end nodes are in the graph
    if start not in graph or end not in graph:
        logging.error(f"Invalid start or end node: {start}, {end}")
        return jsonify({"error": "Invalid start or end node"}), 400

    # Run Dijkstra's algorithm
    result = dijkstra(graph, start, end)

    # Check if no valid path is found
    if result["distance"] == float('inf'):
        logging.warning(f"No path found from {start} to {end}")
        return jsonify({"error": "No path found between the nodes"}), 404

    logging.info(f"Path found: {result}")
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
