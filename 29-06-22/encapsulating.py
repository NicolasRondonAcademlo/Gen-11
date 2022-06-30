class Facturing:
    def __init__(self, type_facture: bool, price_facture: int, id_user: str) -> None:
        self.type_facture = type_facture
        self.price = price_facture
        self.__id_user = id_user

    def show_price(self):
        self.__apply_discount()
        return f"El precio final de la factura es de {self.price}"

    def __apply_discount(self):
        if self.type_facture == True:
            self.price = self.price * 0.7




primer_factura = Facturing(False, 100,"user-54144")
final =primer_factura.show_price()
print(final)


