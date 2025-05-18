from model.model import Model

model = Model()
model.buildGraph("White", 2018)
print(model.getNumNodesEdges())
lista = model._graph.edges
nodo = model._idProducts[94110]
model.ricorsione([], nodo)
print(model.percorso)

