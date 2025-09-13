import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        self._model.build_graph(self._view._ddAnno.value)
        nNodes, nEdges = self._model.get_graph_details()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nNodes}  , Numero di archi: {nEdges}"))
        bestDriver, bestScore = self._model.get_best_pilot()
        self._view.txt_result.controls.append(ft.Text(f"Best Driver : {bestDriver} ,con punteggio :{bestScore}"))
        self._view.update_page()

    def handleCerca(self, e):
        DimTeam = self._view._txtIntK.value
        dreamTeam = self._model.search_dream_team(int(DimTeam))
        componenti , punteggio = self._model.get_Dteam_details()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Dream Team di dimensione {DimTeam} ha punteggio di {punteggio}"))
        self._view.txt_result.controls.append(ft.Text(f"Dream Team di dimensione {DimTeam} è composto da {componenti}"))
        self._view.update_page()

    def fillDDYear(self):
        years = self._model.getYears()

        for y in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(y))