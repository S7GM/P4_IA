import networkx as nx
import matplotlib.pyplot as plt
import time

def dibujar_grafo(G, mst_edges, step):
    plt.clf()
    pos = nx.spring_layout(G, seed=42)

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=600, node_color="#6aa4ff")
    
    # Dibujar todas las aristas en gris
    nx.draw_networkx_edges(G, pos, edge_color="lightgray", width=2)

    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

    # Dibujar pesos
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Dibujar las aristas del MST en color
    if mst_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=mst_edges,
            width=3,
            edge_color="red"
        )

    plt.title(f"Árbol Parcial Mínimo - Paso {step}")
    plt.pause(1)


def prim_grafico(G, inicio):
    visitados = {inicio}
    mst_edges = []
    step = 1

    dibujar_grafo(G, mst_edges, step)

    while len(visitados) < len(G):
        candidatos = []

        for u in visitados:
            for v in G.neighbors(u):
                if v not in visitados:
                    peso = G[u][v]['weight']
                    candidatos.append((peso, u, v))

        if not candidatos:
            print("El grafo no es conexo.")
            return

        candidatos.sort()
        peso, u, v = candidatos[0]

        print(f"Paso {step}: agregando arista {u} -- {v} (peso = {peso})")

        mst_edges.append((u, v))
        visitados.add(v)

        step += 1
        dibujar_grafo(G, mst_edges, step)

    print("\nÁrbol Parcial Mínimo completo:")
    for e in mst_edges:
        print(f"{e[0]} -- {e[1]} (peso = {G[e[0]][e[1]]['weight']})")


def main():
    # Grafo igual al de tu ejemplo
    edges = [
        ("A", "C", 2),
        ("A", "B", 4),
        ("C", "B", 1),
        ("C", "D", 8),
        ("B", "D", 5),
        ("D", "E", 2),
        ("C", "E", 10),
        ("E", "F", 3),
        ("D", "F", 6)
    ]

    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    inicio = input("Nodo inicial: ").upper().strip()
    prim_grafico(G, inicio)

    print("\nSimulación finalizada.")
    plt.show()


if __name__ == "__main__":
    plt.ion()  # modo interactivo
    main()
A
