import copy

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.allNodes=[]
        self._idMapPiloti={}
        self._graph= nx.DiGraph()

        self.best_score=0
        self.dream_team=[]

    def getYears(self):
        years=DAO.get_years()
        return years

    def build_graph(self,anno):
        self._graph.clear()
        nodes= DAO.get_nodes(anno)
        for n in nodes:
            self.allNodes.append(n)
            self._idMapPiloti[n.driverID]=n
            self._graph.add_nodes_from(nodes)

        archi= DAO.getDriverYearResults(anno, self._idMapPiloti)
        for a in archi:
            self._graph.add_edge(a[0],a[1], weight=a[2])

    def get_graph_details(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def get_best_pilot(self):
        bestScore = 0
        bestDriver = None
        for n in self._graph.nodes():
            score = 0
            for e in self._graph.out_edges(n, data=True):
                score += e[2]['weight']
            for e in self._graph.in_edges(n, data=True):
                score -= e[2]['weight']
            if score > bestScore :
                bestScore= score
                bestDriver= n
        return bestDriver, bestScore

    def search_dream_team(self,k):
        self.best_score = 1000
        self.dream_team = []

        parziale =[]
        self.ricorsione(parziale,k)
        return self.dream_team,  self.best_score

    def ricorsione(self,parziale,k):
        if len(parziale)==k:
            score = self.calcola_score(parziale)
            if score < self.best_score:
                self.best_score=score
                self.dream_team=copy.deepcopy(parziale)
            return

        for n in self._graph.nodes():
            if n not in parziale:
                parziale.append(n)
                self.ricorsione(parziale,k)
                parziale.pop()

    def calcola_score(self, team):
        score=0
        for d in self._graph.edges(data = True):
            if d[0] not in team and d[1] in team:
                score += d[2]['weight']

        return score

    def get_Dteam_details(self):
        return self.dream_team, self.best_score



