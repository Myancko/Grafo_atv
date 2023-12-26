import heapq #algoritmo de fila de prioridade
import networkx as nx
import matplotlib.pyplot as plt
import time

start_time = time.time()

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous = {node: None for node in graph}
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node == end:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    path = []
    while end:
        path.append(end)
        end = previous[end]
    return path[::-1]

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
start_node = '2'
end_node = '14'
shortest_path = dijkstra(graph, start_node, end_node)

G = nx.Graph()


for node in graph:
    G.add_node(node)


for node, edges in graph.items():
    for edge, weight in edges.items():
        G.add_edge(node, edge, weight=weight)

pos = nx.spring_layout(G, seed=100)


edge_colors = ['black' if not edge in zip(shortest_path, shortest_path[1:]) else 'red' for edge in G.edges()]
node_colors = ['red' if node in shortest_path else 'blue' for node in G.nodes()]


nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=500, font_weight='bold')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True) if 'weight' in d}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

end_time = time.time()
execution_time = end_time - start_time

print(f"Shortest path: {shortest_path}")
print(f"Execution time: {execution_time} seconds")

plt.show()
