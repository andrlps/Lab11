import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._year = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._color = None
        self._listYear = []
        self._listColor = []
        self._p = None

    def fillDD(self):
        pass


    def handle_graph(self, e):
        self._year = self._view._ddyear.value
        self._color = self._view._ddcolor.value
        self._view.txtOut.controls.clear()
        self.fillDDProduct()
        if self._year is None or self._color is None:
            self._view.txtOut.controls.append(ft.Text("Selezionare un anno e un colore.", color="red"))
            self._view.update_page()
            return
        self._model.buildGraph(self._color, self._year)
        nodes, edges = self._model.getNumNodesEdges()
        self._view.txtOut.controls.append(ft.Text(f"Nodi: {nodes}, Archi: {edges}"))
        edges = self._model.getListEdges()
        for i in range(0,3):
            self._view.txtOut.controls.append(ft.Text(f"Arco da {edges[i].p1} a {edges[i].p2}, peso = {edges[i].weight}"))
        self._view.update_page()

    def fillDDProduct(self):
        for p in self._model.getAllProducts(self._color):
            self._view._ddnode.options.append(ft.dropdown.Option(key=p.Product_number, data=p, on_click=self.pickProduct))
        self._view.update_page()


    def handle_search(self, e):
        self._view.txtOut2.controls.clear()
        if self._p is None:
            self._view.txtOut.controls.append(ft.Text("Selezionare un prodotto", color="red"))
            self._view.update_page()
            return



    def fillYears(self):
        self._listYear = [2015,2016,2017,2018]
        for i in range(2015,2019):
            self._view._ddyear.options.append(ft.dropdown.Option(i))
        self._view.update_page()

    def fillColors(self):
        self._listColor = self._model.getColors()
        for c in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))
        self._view.update_page()

    def pickProduct(self, e):
        self._p = e.control.data
