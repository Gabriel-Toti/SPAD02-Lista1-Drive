from datetime import date
from interfaces.database_table import DatabaseTable

class Order(DatabaseTable):
    def __init__(self,
        order_id: int, customer_id: str, employee_id: int, order_date: date,
        required_date: date=None, shipped_date: date=None, freight: float=None, ship_name: str=None,
        ship_address: str=None, ship_city: str=None, ship_region: str=None, ship_postal_code: str=None,
        ship_country: str=None, shipper_id: int=None):
        
        self._order_id = order_id
        self._customer_id = customer_id
        self._employee_id = employee_id
        self._order_date = order_date
        self._required_date = required_date
        self._shipped_date = shipped_date
        self._freight = freight
        self._ship_name = ship_name
        self._ship_address = ship_address
        self._ship_city = ship_city
        self._ship_region = ship_region
        self._ship_postal_code = ship_postal_code
        self._ship_country = ship_country
        self._shipper_id = shipper_id
        

    @property
    def order_id(self):
        return self.__order_id
    
    @property
    def customer_id(self):
        return self.__customer_id
    
    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def order_date(self):
        return self.__order_date
    
    @property
    def required_date(self):
        return self.__required_date
    
    @property
    def shipped_date(self):
        return self.__shipped_date
    
    @property
    def freight(self):
        return self.__freight
    
    @property
    def ship_name(self):
        return self.__ship_name
    
    @property
    def ship_address(self):
        return self.__ship_address
    
    @property
    def ship_city(self):
        return self.__ship_city
    
    @property
    def ship_region(self):
        return self.__ship_region
    
    @property
    def ship_postal_code(self):
        return self.__ship_postal_code
    
    @property
    def ship_country(self):
        return self.__ship_country
    
    @property
    def shipper_id(self):
        return self.__shipper_id
    
    @order_id.setter
    def _order_id(self, order_id: int):
        self.__order_id = order_id
    
    @customer_id.setter
    def _customer_id(self, customer_id: str):
        if(len(customer_id) > 5):
            raise ValueError("Limite de caracteres excedido para customer_id. max(5).")
        
        self.__customer_id = customer_id

    @employee_id.setter
    def _employee_id(self, employee_id: int):
        self.__employee_id = employee_id
    
    @order_date.setter
    def _order_date(self, order_date: date):
        self.__order_date = order_date
    
    @required_date.setter
    def _required_date(self, required_date: date):
        self.__required_date = required_date
    
    @shipped_date.setter
    def _shipped_date(self, shipped_date: date):
        self.__shipped_date = shipped_date
    
    @freight.setter
    def _freight(self, freight: float):
        self.__freight = freight
    
    @ship_name.setter
    def _ship_name(self, ship_name: str):
        if(ship_name is not None and len(ship_name) > 35):
            raise ValueError("Limite de caracteres excedido para ship_name. max(35).")
        
        self.__ship_name = ship_name
    
    @ship_address.setter
    def _ship_address(self, ship_address: str):
        if(ship_address is not None and len(ship_address) > 50):
            raise ValueError("Limite de caracteres excedido para ship_address. max(50).")
        self.__ship_address = ship_address
    
    @ship_city.setter
    def _ship_city(self, ship_city: str):
        if(ship_city is not None and len(ship_city) > 15):
            raise ValueError("Limite de caracteres excedido para ship_city. max(15).")
        self.__ship_city = ship_city
    
    @ship_region.setter
    def _ship_region(self, ship_region: str):
        if(ship_region is not None and len(ship_region) > 15):
            raise ValueError("Limite de caracteres excedido para ship_region. max(15).")
        self.__ship_region = ship_region
    
    @ship_postal_code.setter
    def _ship_postal_code(self, ship_postal_code: str):
        if(ship_postal_code is not None and len(ship_postal_code) > 9):
            raise ValueError("Limite de caracteres excedido para ship_postal_code. max(9).")
        self.__ship_postal_code = ship_postal_code
    
    @ship_country.setter
    def _ship_country(self, ship_country: str):
        if(ship_country is not None and len(ship_country) > 15):
            raise ValueError("Limite de caracteres excedido para ship_country. max(15).")
        self.__ship_country = ship_country
    
    @shipper_id.setter
    def _shipper_id(self, shipper_id: int):
        self.__shipper_id = shipper_id