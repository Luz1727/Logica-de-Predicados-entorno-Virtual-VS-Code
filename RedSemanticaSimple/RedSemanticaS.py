import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()



# Agregar nodos (conceptos)
G.add_nodes_from(["Perro", "Gato", "Mamífero", "Animal", "Ladra", "Maulla"])

# Agregar relaciones (aristas etiquetadas)
relaciones = [
    ("Perro", "Mamífero", "es un"),
    ("Gato", "Mamífero", "es un"),
    ("Mamífero", "Animal", "es un"),
    ("Perro", "Ladra", "tiene propiedad"),
    ("Gato", "Maulla", "tiene propiedad")
]

for origen, destino, etiqueta in relaciones:
    G.add_edge(origen, destino, relación=etiqueta)

# Mostrar nodos
print("\nNodos en la Red Semántica:")
for nodo in G.nodes:
    print(f"- {nodo}")

# Mostrar relaciones
print("\nRelaciones en la Red Semántica:")
for origen, destino in G.edges:
    print(f"{origen} → ({G[origen][destino]['relación']}) → {destino}")


