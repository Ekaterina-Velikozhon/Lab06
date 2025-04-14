import flet as ft

from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer_code = None

    def populateDDAnno(self):
        anni = self._model.getYear()
        for a in anni:
            self._view.ddAnno.options.append(ft.dropdown.Option(a[0]))
        self._view.update_page()

    def readAnno(self, e):
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

    def populateDDBrand(self):
        brands = self._model.getBrand()
        for b in brands:
            self._view.ddBrand.options.append(ft.dropdown.Option(b[0]))
        self._view.update_page()

    def readBrand(self, e):
        if e.control.value == "None":
            self._brand = None
        else:
            self._brand = e.control.value

    def populateDDRetailer(self):
        retailers = self._model.getRetailer()
        for r in retailers:
            self._view.ddRetailer.options.append(ft.dropdown.Option(r[0]))
        self._view.update_page()

    def readRetailer(self, e):
        if e.control.value == "None":
            self._retailer_code = None
        else:
            self._retailer_code = e.control.value

    def handleTopVendite(self,e):
        top_vendite = self._model.getTopSales(self._anno, self._brand, self._retailer_code)

        self._view.lvTxtOut.controls.clear()
        if len(top_vendite) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for v in top_vendite:
                self._view.lvTxtOut.controls.append(ft.Text(v))

        self._view.update_page()

    def handleAnalizzaVendite(self, e):
        statistica_vendite = self._model.getStatisticSales(self._anno, self._brand, self._retailer_code)

        self._view.lvTxtOut.controls.clear()
        self._view.lvTxtOut.controls.append(ft.Text("Statistiche vendite:"))
        self._view.lvTxtOut.controls.append(ft.Text(f"Giro d'affari: {statistica_vendite[0]}"))
        self._view.lvTxtOut.controls.append(ft.Text(f"Numero vendite: {statistica_vendite[1]}"))
        self._view.lvTxtOut.controls.append(ft.Text(f"Numero retailers coinvolti: {statistica_vendite[2]}"))
        self._view.lvTxtOut.controls.append(ft.Text(f"Numero prodotti coinvolti: {statistica_vendite[3]}"))
        self._view.update_page()


