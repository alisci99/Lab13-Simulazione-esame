from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.allNodes=[]
        self._idMapPiloti={}
        self._graph= nx.DiGraph()

    def getYears(self):
        years=DAO.get_years()
        return years

    def build_garph(self,anno):
        self._graph.clear()
        nodes= DAO.get_nodes(anno)
        for n in nodes:
            self.allNodes.append(n)
            self._idMapPiloti[n.driverID]=n
            self._graph.add_nodes_from(nodes)

        archi= DAO.getDriverYearResults(anno, self._idMapPiloti)
        for a in archi:
            self._graph.add_edge(a[0],a[1], weight=a[2])
