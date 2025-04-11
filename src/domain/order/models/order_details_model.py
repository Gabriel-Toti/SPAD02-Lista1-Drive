from interfaces.database_table import DatabaseTable
class OrderDetails(DatabaseTable):
    def __init__(self,
        order_id: int, product_id: int, unit_price: float, quantity: int, discount: float):
        
        self._order_id = order_id
        self._product_id = product_id
        self._unit_price = unit_price
        self._quantity = quantity
        self._discount = discount

    @property
    def order_id(self):
        return self.__order_id

    @property
    def product_id(self):
        return self.__product_id

    @property
    def unit_price(self):
        return self.__unit_price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def discount(self):
        return self.__discount

    @order_id.setter
    def _order_id(self, order_id: int):
        self.__order_id = order_id

    @product_id.setter
    def _product_id(self, product_id: int):
        self.__product_id = product_id

    @unit_price.setter
    def _unit_price(self, unit_price: float):
        self.__unit_price = unit_price

    @quantity.setter
    def _quantity(self, quantity: int):
        self.__quantity = quantity

    @discount.setter
    def _discount(self, discount: float):
        self.__discount = discount
