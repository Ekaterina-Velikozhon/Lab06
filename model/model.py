from database.DAO import DAO

class Model:
    def __init__(self):
        self._dao = DAO()

    def getYear(self):
        return self._dao.getYear()

    def getBrand(self):
        return self._dao.getBrand()

    def getRetailer(self):
        return self._dao.getRetailer()

    def getTopSales(self, anno, brand, retailer_code):
        res = self._dao.getTopSales(anno, brand, retailer_code)
        return res[0:5]

    def getStatisticSales(self, anno, brand, retailer_code):
        res = self._dao.getTopSales(anno, brand, retailer_code)
        ricavo_totale = sum([sale.ricavo for sale in res])
        retailer_coinvolti = set([sale.retailer_code for sale in res]) #oppure {sale.retailer_code for sale in res}
        prodotti_coinvolti = set([sale.product_number for sale in res])
        return ricavo_totale, len(res), len(retailer_coinvolti), len(prodotti_coinvolti) #mi restituisce una TUPLA