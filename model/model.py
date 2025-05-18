import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._idProducts = {}
        self._graph = None
        self._edges = None
        self.percorso = 0

    def getColors(self):
        return DAO.getColors()

    def buildGraph(self, color, year):
        self._graph = nx.Graph()
        self._graph.add_nodes_from(self.getAllProducts(color))
        self.getAllEdges(color, year)

    def getAllProducts(self, color):
        plist = DAO.getAllProducts(color)
        for p in plist:
            self._idProducts[p.Product_number] = p
        return plist

    def getAllEdges(self, color, year):
        self._edges =  DAO.getAllEdges(color, year, self._idProducts)
        for e in self._edges:
            self._graph.add_edge(e.p1, e.p2, weight=e.weight)

    def getNumNodesEdges(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getListEdges(self):
        return self._edges

    def getPercorso(self, nodo):
        self.ricorsione([], nodo)
        return self.percorso

    def ricorsione(self, parziale, nodo):
        if self.fine(parziale, nodo):
            if len(parziale) > self.percorso:
                self.percorso = len(parziale)
        else:
            for n in self._graph.neighbors(nodo):
                if self.condizione(parziale, nodo, n):
                    parziale.append((nodo, n, self._graph[nodo][n]["weight"]))
                    self.ricorsione(parziale, n)
                    parziale.pop()

    def condizione(self, parziale, nodo, n):
        if len(parziale) == 0:
            return True
        ultimoPeso = parziale[-1][2]
        if ultimoPeso <= self._graph[nodo][n]["weight"] and parziale[-1][0] != n:
            return True
        return False

    def fine(self, parziale, nodo):
        if len(parziale) == 0:
            return False
        for n in self._graph.neighbors(nodo):
            ultimoPeso = parziale[-1][2]
            if ultimoPeso < self._graph[nodo][n]["weight"]:
                return False
        return True

