import networkx as nx

from database.DAO import DAO
from model.arco import Arco


class Model:
    def __init__(self):
        self._graph = None
        self._idProducts = {}

    def getColori(self):
        colors = DAO.getColori()
        colors.sort()
        return colors

    def buildGraph(self, y, c):
        self._graph = nx.Graph()
        nodes = DAO.getAllNodes(c)
        self._graph.add_nodes_from(nodes)
        for n in nodes:
            self._idProducts[n.Product_number] = n
        edges = DAO.getAllEdges(self._idProducts, y, c)
        for e in edges:
            if self._graph.has_edge(e.p1, e.p2):
                self._graph[e.p1][e.p2]["weight"]+=e.peso
            else:
                self._graph.add_edge(e.p1,e.p2,weight=e.peso)
        print(self._graph.number_of_edges())

    def infoGraph(self):
        return self._graph.number_of_nodes, self._graph.number_of_edges

    def archiPeso(self):
        archi = []
        for u in self._graph.nodes():
            for v in self._graph.nodes():
                archi.append((u,v,self._graph[u][v]["weight"]))
        archi.sort(key=lambda x: x[2], reverse = True)
        return archi



