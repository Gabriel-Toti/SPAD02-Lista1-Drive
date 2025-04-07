class AddressedEntity():
    def __init__(self, address: str, city: str, region: str, postal_code: str, country: str):
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
        self.__address = address

    @city.setter
    def _city(self, city: str):
        self.__city = city
    
    @region.setter
    def _region(self, region: str):
        self.__region = region

    @postal_code.setter
    def _postal_code(self, postal_code: str):
        self.__postal_code = postal_code
    
    @country.setter
    def _country(self, country: str):
        self.__country = country