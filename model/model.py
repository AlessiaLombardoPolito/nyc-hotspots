import networkx as nx

from database.DAO import DAO
from geopy.distance import distance


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._allProviders= DAO.getAllProvider()

    def getProviders(self):
        return self._allProviders

    def getNodes(self):
        pass

    def getEdges(self):
        pass

    def buildGraph(self, provider, soglia):
        self._nodes = DAO.getLocationsOfProviderV2(provider)
        self._grafo.add_nodes_from(self._nodes)

        # #Add edges
        # #MODO 1: faccio una query che mi restisce gli archi.
        # allEdges = DAO.getAllEdges(provider)
        # for edge in allEdges:
        #     l1 = edge[0]
        #     l2 = edge[1]
        #     dist = distance((l1.latitude, l1.longitude), (l2.latitude, l2.longitude)).km
        #     if dist < soglia:
        #         self._graph.add_edge(l1, l2, weight=dist)
        #
        # print(f"Modo 1: N nodes: {len(self._graph.nodes)} - N edges: {len(self._graph.edges)}")
        #
        # self._graph.clear_edges()

        # MODO 2: modifico il metodo del dao che legge i nodi,
        # e ci aggiungo le coordinate di ogni location
        # Dopo, doppio ciclo sui nodi, e mi calcolo le distanza in python
        for u in self._nodes:
            for v in self._nodes:
                if u != v:
                    dist = distance((u.latitude, u.longitude), (v.latitude, v.longitude)).km
                    if dist < soglia:
                        self._grafo.add_edge(u, v, weight=dist)

        print(f"Modo 2: N nodes: {len(self._grafo.nodes)} - N edges: {len(self._grafo.edges)}")

        # MODO 3: Doppio ciclo sui nodi, e per ogni "possibile" arco, faccio una query.

    def getGraphInfo(self):
        numNodi = self._grafo.number_of_nodes()
        #numArchi = self._grafo.number_of_edges()
        return numNodi