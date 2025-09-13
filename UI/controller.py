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
        self._model.build_garph(self._view._ddAnno.value)
        nNodes, nEdges = self._model.get_graph_details()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nNodes}  , Numero di archi: {nEdges}"))
        self._view.update_page()

    def handleCerca(self, e):
        pass

    def fillDDYear(self):
        years = self._model.getYears()

        for y in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(y))