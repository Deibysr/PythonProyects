def dfs(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)
    return visitado

# Ejemplo de uso
grafo = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visitado = dfs(grafo, 'A')
print("Nodos visitados:", visitado)
