import itertools
import networkx as nx
import matplotlib.pyplot as plt


def buscar_caminhos(graph):
    """
    Essa função procura por todos os caminhos, que passam por todos os pontos do grafo sem se repitir
    """
    caminhos_com_pesos = []

    nodes = list(graph.nodes())
    all_paths = itertools.permutations(nodes)

    #print(all_paths)
    #input('<stop>')

    for path in all_paths:
        
        #print(path[0])
        #if int(path[0]) != 1: #para iterar apenas nas possibilidades do primeiro digito
        #    return caminhos_com_pesos
        
        peso = 0
        valid_path = True
        for i in range(len(path) - 1):
            if graph.has_edge(path[i], path[i + 1]):
                peso += graph[path[i]][path[i + 1]]['weight']
            else:
                valid_path = False
                break 
            
        if valid_path:
            caminhos_com_pesos.append((list(path), peso))

    return caminhos_com_pesos

grafo = nx.Graph()
grafo.add_nodes_from(['1', '2', '3', '4', '5'])
grafo.add_edges_from([('1', '2', {'weight': 2}), ('1', '4', {'weight': 3}), ('1', '5', {'weight': 6}),
                      ('2', '4', {'weight': 3}), ('2', '3', {'weight': 4}), ('3', '5', {'weight': 3}),
                      ('3', '4', {'weight': 7}), ('4', '5', {'weight': 3})])

caminhos_com_pesos = buscar_caminhos(grafo)

menor = -1

for caminho in caminhos_com_pesos:
    #percorre todos os caminhos para buscar qual possui o menor peso
    if menor == -1:
        menor = caminho
    elif menor[1] > int(caminho[1]):
        menor = caminho
        
plt.figure(figsize=(8, 6))

count = 0
for caminho in caminhos_com_pesos:
    
    count += 1
    print(f"caminho {count}: {caminho}")

peso_menor = menor[1]

pos = nx.spring_layout(grafo)
edge_labels = {(u, v): d['weight'] for u, v, d in grafo.edges(data=True)}
arestas_caminho_menor_peso = [(menor[0][i], menor[0][i+1]) for i in range(len(menor[0])-1)]

print(arestas_caminho_menor_peso, peso_menor)

nx.draw(grafo, pos=pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold', font_size=12)  #desenha o grafo inicial
nx.draw_networkx_edges(grafo, pos=pos, edgelist=arestas_caminho_menor_peso, edge_color='red', width=2) #desenha caminho mais curto
nx.draw_networkx_edge_labels(grafo, pos=pos, edge_labels=edge_labels) # desenha o peso de cada caminho sobre o que ja foi desenhado

plt.text(0.90,
         0.95,
         f'Menor peso: {peso_menor}',
         horizontalalignment='center',
         verticalalignment='center',
         transform=plt.gca().transAxes, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.show()