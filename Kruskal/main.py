import networkx as nx
import matplotlib.pyplot as plt
import time

start_time = time.time()

def kruskal(graph):
    mst = []
    edges = []

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edges.append((weight, node, neighbor))

    edges.sort()

    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        parent[root_u] = root_v

    for weight, u, v in edges:
        if find(u) != find(v):
            mst.append((u, v))
            union(u, v)

    return mst

def calculate_height(graph, minimum_spanning_tree):
    def dfs(node, visited):
        visited.add(node)
        max_height = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                height = dfs(neighbor, visited)
                max_height = max(max_height, height)
        return max_height + 1

    heights = []
    for start_node, end_node in minimum_spanning_tree:
        visited = set()
        height = dfs(start_node, visited)
        heights.append(height)
        visited = set()
        height = dfs(end_node, visited)
        heights.append(height)

    return max(heights)

graph = {
    '1': {'2': 20, '12': 29, '8': 29},
    '2': {'3': 25, '8': 28, '12': 39},
    '3': {'4': 25, '8': 30, '13': 54},
    '4': {'9': 23, '10': 33, '5': 39, '6': 32, '7': 42, '14': 56},
    '5': {'10': 19, '6': 12, '7': 26},
    '6': {'11': 30, '10': 35, '7': 17},
    '7': {'11': 38},
    '8': {'12': 25, '13': 22},
    '9': {'13': 34, '10': 26, '14': 0, '16': 43},
    '10': {'11': 24, '15': 19, '14': 20},
    '11': {'18': 36, '15': 26},
    '12': {'13': 27, '16': 43},
    '13': {'16': 19, '14': 24},
    '14': {'16': 19, '17': 17, '15': 20},
    '15': {'17': 18, '18': 21},
    '16': {'17': 26},
    '17': {'18': 15},
    '18': {}
}

minimum_spanning_tree = kruskal(graph)

G = nx.Graph()


for node in graph:
    G.add_node(node)

for node, edges in graph.items():
    for edge, weight in edges.items():
        G.add_edge(node, edge, weight=weight)

pos = nx.spring_layout(G)

edge_colors = ['black' for edge in G.edges()]
node_colors = ['Yellow' for node in G.nodes()]

for u, v in minimum_spanning_tree:
    G[u][v]['color'] = 'red'

edges = G.edges()
colors = [G[u][v].get('color', 'black') for u, v in edges]

nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=colors, node_size=500, font_weight='bold')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True) if 'weight' in d}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

end_time = time.time()
execution_time = end_time - start_time

height = calculate_height(graph, minimum_spanning_tree)
print(f"Height of the minimum spanning tree: {height}")

print(f"Execution time: {execution_time} seconds")

plt.show()
