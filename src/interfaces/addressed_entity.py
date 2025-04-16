class AddressedEntity():
    def __init__(self, address: str=None, city: str=None, region: str=None, postal_code: str=None, country: str=None):
        self._address = address
        self._city = city
        self._region = region
        self._postal_code = postal_code
        self._country = country
    
    @property
    def address(self):
        return self.__address
    
    @property
    def city(self):
        return self.__city
    
    @property
    def region(self):
        return self.__region
    
    @property
    def postal_code(self):
        return self.__postal_code
    
    @property
    def country(self):
        return self.__country
    
    @address.setter
    def _address(self, address: str):
        if(address is not None and len(address) > 50):
            raise ValueError("Limite de caracteres excedido para address. max(50).")
        self.__address = address

    @city.setter
    def _city(self, city: str):
        if(city is not None and len(city) > 20):
            raise ValueError("Limite de caracteres excedido para city. max(20).")
        self.__city = city
    
    @region.setter
    def _region(self, region: str):
        if(region is not None and len(region) > 2):
            raise ValueError("Limite de caracteres excedido para region. max(2).")
        self.__region = region

    @postal_code.setter
    def _postal_code(self, postal_code: str):
        if(postal_code is not None and len(postal_code) > 9):
            raise ValueError("Limite de caracteres excedido para postal_code. max(9).")
        self.__postal_code = postal_code
    
    @country.setter
    def _country(self, country: str):
        if(country is not None and len(country) > 15):
            raise ValueError("Limite de caracteres excedido para country. max(15).")
        self.__country = country