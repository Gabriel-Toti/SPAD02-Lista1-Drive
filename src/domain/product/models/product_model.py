class Product():
    def __init__(self,
        product_id: int, product_name: str, supplier_id: int, category_id: int,
        quantity_per_unit: str, unit_price: float, units_in_stock: int,
        units_on_order: int, reorder_level: int, discontinued: str):
        
        self._product_id = product_id
        self._product_name = product_name
        self._supplier_id = supplier_id
        self._category_id = category_id
        self._quantity_per_unit = quantity_per_unit
        self._unit_price = unit_price
        self._units_in_stock = units_in_stock
        self._units_on_order = units_on_order
        self._reorder_level = reorder_level
        self._discontinued = discontinued

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @property
    def supplier_id(self):
        return self.__supplier_id

    @property
    def category_id(self):
        return self.__category_id

    @property
    def quantity_per_unit(self):
        return self.__quantity_per_unit

    @property
    def unit_price(self):
        return self.__unit_price

    @property
    def units_in_stock(self):
        return self.__units_in_stock

    @property
    def units_on_order(self):
        return self.__units_on_order

    @property
    def reorder_level(self):
        return self.__reorder_level

    @property
    def discontinued(self):
        return self.__discontinued

    @product_id.setter
    def _product_id(self, product_id: int):
        self.__product_id = product_id

    @product_name.setter
    def _product_name(self, product_name: str):
        self.__product_name = product_name

    @supplier_id.setter
    def _supplier_id(self, supplier_id: int):
        self.__supplier_id = supplier_id

    @category_id.setter
    def _category_id(self, category_id: int):
        self.__category_id = category_id

    @quantity_per_unit.setter
    def _quantity_per_unit(self, quantity_per_unit: str):
        self.__quantity_per_unit = quantity_per_unit

    @unit_price.setter
    def _unit_price(self, unit_price: float):
        self.__unit_price = unit_price

    @units_in_stock.setter
    def _units_in_stock(self, units_in_stock: int):
        self.__units_in_stock = units_in_stock

    @units_on_order.setter
    def _units_on_order(self, units_on_order: int):
        self.__units_on_order = units_on_order

    @reorder_level.setter
    def _reorder_level(self, reorder_level: int):
        self.__reorder_level = reorder_level

    @discontinued.setter
    def _discontinued(self, discontinued: str):
        self.__discontinued = discontinued
