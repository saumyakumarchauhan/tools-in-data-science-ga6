
# 🔗 Network Analysis: Shortest Path in Social Network Graph

This guide helps you find the **shortest path** between two users in a **weighted, undirected social network graph**, using **Python** and **NetworkX**.

---

## 📁 Dataset Details

- File: `network_graph.json`
- Nodes: Represent users (e.g., `user_0`, `user_1`, ..., `user_987`)
- Edges: Represent professional connections
- Weights: Connection strength (1 = strongest, 10 = weakest)
- Graph Type: Undirected, Weighted

---

## 🎯 Problem

Each student is assigned a different task to **find the shortest path** between two specific users.

> Example:
> 
> Find the shortest path from `user_120` to `user_632`.  
> (For you, this pair might be different — use your assigned users.)

---

## 🛠️ Requirements

Install `networkx` (if not already installed):

```bash
pip install networkx
```

---

## 🚀 Full Working Code

```python
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
    print("🔗 Shortest Path (Arrow format):", " -> ".join(shortest_path))
    print("📋 Comma-separated:", ", ".join(shortest_path))
    print("🔣 Space-separated:", " ".join(shortest_path))
    print("📦 Python List:", shortest_path)
    print("📏 Total Connection Strength (lower is better):", total_weight)

except nx.NetworkXNoPath:
    print(f"No path found between {source_user} and {target_user}")
```

---

## ✅ Accepted Answer Formats

Submit your answer in **any one** of the following formats:

- `user_1 -> user_5 -> user_8`
- `user_1, user_5, user_8`
- `user_1 user_5 user_8`
- `['user_1', 'user_5', 'user_8']`

---

## ⚠️ Notes

- The graph is **undirected** (connections go both ways).
- The path is calculated using **edge weights** (Dijkstra’s algorithm).
- Lower weight = **stronger** professional connection.
- Replace only the `source_user` and `target_user` values with the ones assigned to you.
