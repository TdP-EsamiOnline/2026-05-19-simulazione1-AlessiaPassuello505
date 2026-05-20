import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        generi = self._model.getGeneri()
        generiDD = []
        for g in generi:
            generiDD.append(ft.dropdown.Option(g))

        # yearsDD = list(map(lambda x: ft.dropdown.Option(x), years))
        self._view._ddGenre.options = generiDD
        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._model.creaGrafo()
        n, m = self._model.getGraphDetails()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato! "
                    f"Il grafo è costituito di {n} nodi ed {m} archi"))

        self._view.update_page()

    def handleCreaGrafo(self,e):
        pass

    def handleCammino(self,e):
        pass