from flask import Flask, request, jsonify
from algorithms.dijkstra import dijkstra
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
import json
import os

app = Flask(__name__)

def load_graph():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'graph.json')
    with open(file_path, 'r') as f:
        return json.load(f)

graph = load_graph()

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Server is running!"})

@app.route("/<algorithm>", methods=["POST"])
def shortest_path(algorithm):
    data = request.get_json()
    start = data.get("start")
    end = data.get("end")

    if start not in graph or end not in graph:
        return jsonify({"error": "Invalid start or end node"}), 400

    if algorithm == "dijkstra":
        result = dijkstra(graph, start, end)
    elif algorithm == "bfs":
        result = bfs(graph, start, end)
    elif algorithm == "dfs":
        result = dfs(graph, start, end)
    elif algorithm == "astar":
        result = astar(graph, start, end)
    else:
        return jsonify({"error": "Unsupported algorithm"}), 400

    if not result["path"]:
        return jsonify({"error": "No path found"}), 404

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
