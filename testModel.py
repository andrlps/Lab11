from model.model import Model

model = Model()
model.buildGraph("Red", 2015)
print(model.getNumNodesEdges())
lista = model._graph.edges
nodo = model._idProducts[12110]
model.ricorsione([], nodo)
print(model.percorso)

