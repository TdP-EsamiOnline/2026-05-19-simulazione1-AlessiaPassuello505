import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.DiGraph()
        self._artisti=[]

    def creaGrafo(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._artisti)


    def getGeneri(self):
        return DAO.getGenere()

    def getArtistiGenere(self,genere):
        self._artisti= DAO.getArtistiGenere(genere)
        return self._artisti

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)