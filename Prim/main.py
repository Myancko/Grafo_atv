import networkx as nx
import matplotlib.pyplot as plt
import time

start_time = time.time()

def prim_mst(graph):
    mst = set()
    vertices = list(graph.keys())
    if not vertices:
        return mst
    
    mst.add(vertices[0])
    mst_edges = []
    
    while len(mst) < len(vertices):
        min_edge = None
        min_weight = float('inf')
        
        for vertex in mst:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in mst and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)
        
        if min_edge:
            mst.add(min_edge[1])
            mst_edges.append(min_edge)
    
    return mst_edges

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

prim = prim_mst(graph)

G = nx.Graph()

# Add nodes
for node in graph:
    G.add_node(node)
    
for edge in prim:
    G.add_edge(edge[0], edge[1], weight=graph[edge[0]][edge[1]])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, font_weight='bold')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True) if 'weight' in d}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

end_time = time.time()
execution_time = end_time - start_time

print(f"Minimum Spanning Tree Edges: {prim}")
print(f"Execution time: {execution_time} seconds")

plt.show()
