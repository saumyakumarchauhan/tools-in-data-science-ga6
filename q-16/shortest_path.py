import json
import networkx as nx

# Load the graph data from JSON file
with open("network_graph.json") as f:
    data = json.load(f)

# Create an undirected graph
G = nx.Graph()

# Add edges with weights to the graph
for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"], weight=edge["weight"])

# --- CHANGE THESE TWO VALUES FOR YOUR ASSIGNMENT ---
source_user = 'user_120'   # Replace with your given source
target_user = 'user_632'   # Replace with your given target
# ---------------------------------------------------

# Compute shortest path using Dijkstra's algorithm
try:
    shortest_path = nx.shortest_path(G, source=source_user, target=target_user, weight="weight")
    total_weight = nx.shortest_path_length(G, source=source_user, target=target_user, weight="weight")

    # Output in different formats
    print(" Shortest Path (Arrow format):", " -> ".join(shortest_path))
    print(" Comma-separated:", ", ".join(shortest_path))
    print(" Space-separated:", " ".join(shortest_path))
    print(" Python List:", shortest_path)
    print(" Total Connection Strength (lower is better):", total_weight)

except nx.NetworkXNoPath:
    print(f"No path found between {source_user} and {target_user}")
