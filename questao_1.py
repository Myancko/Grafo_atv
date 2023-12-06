import itertools
import networkx as nx
import matplotlib.pyplot as plt

def encontrar_caminhos_que_visitem_todos_os_nos(graph):
    caminhos_com_pesos = []

    nodes = list(graph.nodes())
    all_paths = itertools.permutations(nodes)

    for path in all_paths:
        peso = 0
        valid_path = True
        for i in range(len(path) - 1):
            if graph.has_edge(path[i], path[i + 1]):
                peso += graph[path[i]][path[i + 1]]['weight']
            else:
                valid_path = False
                break 
            caminhos_com_pesos.append((list(path), peso))

    return caminhos_com_pesos

grafo = nx.Graph()

grafo.add_node('1')
grafo.add_node('2')
grafo.add_node('3')
grafo.add_node('4')
grafo.add_node('5')

#1
grafo.add_edge('1', '2', weight=2)
grafo.add_edge('1', '4', weight=3)
grafo.add_edge('1', '5', weight=6)
#2
grafo.add_edge('2', '4', weight=3)
grafo.add_edge('2', '3', weight=4)
#3
grafo.add_edge('3', '5', weight=3)
grafo.add_edge('3', '4', weight=7)
#4
grafo.add_edge('4', '5', weight=3)

print(grafo.nodes())

for edge in grafo.edges():
    
    u = edge[0]
    v = edge[1]
    print('peso', edge, 'vale', grafo[u][v]['weight'])

x = nx.adjacency_matrix(grafo)
print(x.todense())

caminhos_com_pesos = encontrar_caminhos_que_visitem_todos_os_nos(grafo)
caminho_menor_peso = min(caminhos_com_pesos, key=lambda x: x[1])

count = 0
for caminho in caminhos_com_pesos:
    
    count += 1
    print(f"caminho {count}: {caminho}")

arestas_caminho_menor_peso = [(caminho_menor_peso[0][i], caminho_menor_peso[0][i+1]) for i in range(len(caminho_menor_peso[0])-1)]

peso_menor = caminho_menor_peso[1]

print('menor caminho:', caminho_menor_peso)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos=pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold', font_size=12)
nx.draw_networkx_edges(grafo, pos=pos, edgelist=arestas_caminho_menor_peso, edge_color='red', width=2)

edge_labels = {(u, v): d['weight'] for u, v, d in grafo.edges(data=True)}
nx.draw_networkx_edge_labels(grafo, pos=pos, edge_labels=edge_labels)

pos_texto_x = 0.85 
pos_texto_7 = 0.97  
plt.text(pos_texto_x, pos_texto_7, f'caminho com menor peso: {peso_menor}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8))

plt.show()