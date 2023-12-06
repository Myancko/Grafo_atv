import os
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def encontrar_caminhos_que_visitem_todos_os_nos(graph):
    caminhos_com_pesos = []

    nodes = list(graph.nodes())
    all_paths = itertools.permutations(nodes)
    count = 1
    count_check = 0
    for path in all_paths:
        os.system('cls')
        print(f'{count_check} ta rodando'+ '.'*count)
        count+=1
        count_check += 1
        if count == 4:
            count = 1
            
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

count =  0

while count < 18:
    count += 1
    grafo.add_node(f'{count}')


#1
grafo.add_edge('1', '2', weight=20)
grafo.add_edge('1', '12', weight=29)
grafo.add_edge('1', '8', weight=29)
#2
grafo.add_edge('2', '3', weight=25)
grafo.add_edge('2', '8', weight=28)
grafo.add_edge('2', '12', weight=39)
#3
grafo.add_edge('3', '4', weight=25)
grafo.add_edge('3', '8', weight=30)
grafo.add_edge('3', '13', weight=54)
#4
grafo.add_edge('4', '9', weight=23)
grafo.add_edge('4', '14', weight=56)
grafo.add_edge('4', '10', weight=33)
grafo.add_edge('4', '5', weight=39)
grafo.add_edge('4', '6', weight=32)
grafo.add_edge('4', '7', weight=42)
#5
grafo.add_edge('5', '10', weight=19)
grafo.add_edge('5', '6', weight=12)
grafo.add_edge('5', '7', weight=26)
#6
grafo.add_edge('6', '11', weight=30)
grafo.add_edge('6', '10', weight=35)
grafo.add_edge('6', '7', weight=17)
#7
grafo.add_edge('7', '11', weight=38)
#8
grafo.add_edge('8', '12', weight=25)
grafo.add_edge('8', '13', weight=22)
#9
grafo.add_edge('9', '13', weight=34)
grafo.add_edge('9', '10', weight=26)
grafo.add_edge('9', '14', weight=0)
grafo.add_edge('9', '16', weight=43)
#10
grafo.add_edge('10', '11', weight=24)
grafo.add_edge('10', '15', weight=19)
grafo.add_edge('10', '14', weight=20)
#11
grafo.add_edge('11', '18', weight=36)
grafo.add_edge('11', '15', weight=26)
#12
grafo.add_edge('12', '13', weight=27)
grafo.add_edge('12', '16', weight=43)
#13
grafo.add_edge('13', '16', weight=19)
grafo.add_edge('13', '14', weight=24)
#14
grafo.add_edge('14', '16', weight=19)
grafo.add_edge('14', '17', weight=17)
grafo.add_edge('14', '15', weight=20)
#15
grafo.add_edge('15', '17', weight=18)
grafo.add_edge('15', '18', weight=21)
#16
grafo.add_edge('16', '17', weight=26)
#17
grafo.add_edge('17', '18', weight=15)

print(grafo.nodes())

for edge in grafo.edges():
    
    u = edge[0]
    v = edge[1]
    print('peso', edge, 'vale', grafo[u][v]['weight'])

x = nx.adjacency_matrix(grafo)
print(x.todense())

print('ta rodando')
caminhos_com_pesos = encontrar_caminhos_que_visitem_todos_os_nos(grafo)
caminho_menor_peso = min(caminhos_com_pesos, key=lambda x: x[1])
print('foi')

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