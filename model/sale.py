import datetime
from dataclasses import dataclass

from model.product import Product
from model.retailer import Retailer

@dataclass()
class Sale:
    #NOTA: NON SCRIVO LE RELAZIONI
    date: datetime.time
    quantity: int
    unit_price: float
    unit_sale_price: float
    #RELAZIONI
    retailer_code: int
    product_number: int
    order_method_code: int
    #Per ogni Sale ho Retailer e Product :)
    retailer: Retailer = None
    product: Product = None

    def __str__(self):
        return f"Data: {self.date}; Ricavo: {self.ricavo}; Retailer: {self.retailer_code}; Product: {self.product_number}"

    def __eq__(self, other): #LA CHIAVE PRIMARIA E' QUELLA CHE COLLEGA SALE CON GLI ALTRI TABELLE
        return (self.retailer_code == other.retailer_code
                and self.product_number == other.product_number
                and self.order_method_code == other.order_method_code)

    def __hash__(self):
        return hash((self.retailer_code, self.product_number, self.order_method_code))

    def __post_init__(self): #DOPO INIZIALIZZAZIONE CALCOLA IL MIO RICAVO
        """
        Calcolo il RICAVO
        """
        self.ricavo: float = self.unit_sale_price * self.quantity

    # def __lt__(self, other): #SORTING DEL RICAVO, viene fatto in automatico
    #     return self.ricavo < other.ricavo

