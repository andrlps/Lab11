import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []
        self._year = None
        self._color = None

    def fillDD(self):
        for i in range(2015,2019):
            self._view._ddyear.options.append(ft.dropdown.Option(i))
        for color in self._model.getColori():
            self._view._ddcolor.options.append(ft.dropdown.Option(color))
        self._view.update_page()


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        self._year = self._view._ddyear.value
        self._color = self._view._ddcolor.value
        if self._color is None or self._year is None:
            self._view.txtOut.controls.append(ft.Text("Selezionare un valore per il campo anno e colore."))
            self._view.update_page()
            return
        self._model.buildGraph(self._year, self._color)
        nNodi, nArchi = self._model.infoGraph()
        self._view.txtOut.controls.append(ft.Text(f"N Nodi: {nNodi}, N archi: {nArchi}"))
        archi = self._model.archiPeso()
        for i in range(0,3):
            self._view.txtOut.controls.append(ft.Text(f"{archi[0]} - {archi[1]}, peso: {archi[2]}"))
        numArchi = {}
        for arco in archi[:3]:
            if numArchi.__contains__(arco[0]):
                numArchi[arco[0]]+=1
            else:
                numArchi[arco[0]] = 1
            if numArchi.__contains__(arco[1]):
                numArchi[arco[1]] += 1
            else:
                numArchi[arco[1]] = 1
        for key in numArchi:
            if numArchi[key]>1:
                self._view.txtOut.controls.append(ft.Text(f"{numArchi[key]}"))




    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
